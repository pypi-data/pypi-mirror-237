import re
import time
import warnings

import torch
import torch.fx as fx
import torch.nn as nn
from typing_extensions import Any, Dict, List, Optional, Tuple, Union

from .module import SohuGraph, SohuModule
from .te_equivalent import DotProductAttention, LayerNormLinear, LayerNormMLP
from .te_equivalent import Linear as TE_Linear
from .te_equivalent import TransformerLayer
from .torch_equivalent import (
    GELU,
    LayerNorm,
    Linear,
    Module,
    ReLU,
    SiLU,
    function_replacements,
)
from .transformations import graph_transformations
from .utils import never, recursive_getattr

_NAME_COUNTS: Dict[str, int] = {}


def _get_unique_name(base_name: str) -> str:
    # Make sure the name is a valid identifier, otherwise convert it to one
    if not base_name.isidentifier():
        # Remove all non-alphanumeric, non-underscore characters
        base_name = re.sub(r"[^a-zA-Z0-9_]", "_", base_name)
        # If it's still not a valid identifier, prepend an underscore
        base_name = base_name if base_name.isidentifier() else "_" + base_name
    global _NAME_COUNTS
    name_count = _NAME_COUNTS.get(base_name, 0)
    _NAME_COUNTS[base_name] = name_count + 1
    return base_name + "_" + str(name_count)


def _te_get_equivalent(module: nn.Module) -> Module:
    import transformer_engine.pytorch as te

    if type(module) == te.Linear:
        params_dtype = module.weight_tensor.dtype
        assert isinstance(
            params_dtype, torch.dtype
        ), f"params_dtype must be a torch.dtype, not a {type(params_dtype)}"
        return TE_Linear(
            module.in_features,
            module.out_features,
            bias=module.use_bias,
            params_dtype=params_dtype,
            parameters_split=module.parameters_split,
        )
    elif type(module) == te.LayerNorm:
        return LayerNorm(module.state_dict()["weight"].shape[0], eps=module.eps)
    elif type(module) == te.LayerNormLinear:
        return LayerNormLinear(
            module.in_features,
            module.out_features,
            bias=module.use_bias,
            eps=module.eps,
            parameters_split=module.parameters_split,
            params_dtype=module.layer_norm_weight.dtype,
        )
    elif type(module) == te.LayerNormMLP:
        return LayerNormMLP(
            module.fc1_weight.shape[1],
            module.fc2_weight.shape[1],
            bias=module.use_bias,
            eps=module.eps,
            activation=module.activation,
        )
    elif type(module) == te.DotProductAttention:
        return DotProductAttention(
            num_attention_heads=module.hidden_size_per_partition
            * module.tp_size
            // module.hidden_size_per_attention_head,
            kv_channels=module.hidden_size_per_attention_head,
            attn_mask_type=module.attn_mask_type,
        )
    elif type(module) == te.attention.MultiHeadAttention:
        raise NotImplementedError()
    elif type(module) == te.TransformerLayer:
        hidden_size, ffn_hidden_size = module.layernorm_mlp.fc2_weight.shape
        assert (
            ffn_hidden_size,
            hidden_size,
        ) == module.layernorm_mlp.fc1_weight.shape, f"The following should be equal: module.layernorm_mlp.fc1_weight.shape = {module.layernorm_mlp.fc1_weight.shape}, (ffn_hidden_size, hidden_size) = {(ffn_hidden_size, hidden_size)}"
        return TransformerLayer(
            hidden_size=hidden_size,
            ffn_hidden_size=ffn_hidden_size,
            num_attention_heads=hidden_size // module.kv_channels,
            layernorm_epsilon=module.layernorm_mlp.eps,
            kv_channels=module.kv_channels,
            params_dtype=module.layernorm_mlp.fc1_weight.dtype,
            bias=module.layernorm_mlp.use_bias,
            activation=module.layernorm_mlp.activation,
        )
    else:
        raise NotImplementedError(
            f"Unsupported transformer_engine module type: {type(module)}"
        )


def get_equivalent(module: nn.Module) -> Optional[Module]:
    if module.__module__.split(".")[0] == "transformer_engine":
        etched_module = _te_get_equivalent(module)
    elif type(module) == nn.Linear:
        etched_module = Linear(
            module.in_features,
            module.out_features,
            bias=module.bias is not None and module.bias.numel() > 0,
        )
    elif type(module) == nn.LayerNorm:
        etched_module = LayerNorm(module.normalized_shape[-1], eps=module.eps)
    elif type(module) == nn.ReLU:
        etched_module = ReLU()
    elif type(module) == nn.GELU:
        etched_module = GELU()
    elif type(module) == nn.SiLU:
        etched_module = SiLU()
    else:
        return None
    missing, unexpected = etched_module.load_state_dict(
        module.state_dict(), strict=False
    )
    if len(missing) > 0:
        warnings.warn(f"Module {module} has missing keys {missing}")
    unexpected = [key for key in unexpected if not "_extra_state" in key]
    if len(unexpected) > 0:
        warnings.warn(f"Module {module} has unexpected keys {unexpected}")
    etched_module.post_load_state_dict()
    return etched_module


def replace_modules(module: nn.Module) -> nn.Module:
    """
    Recursively replaces all modules that have a corresponding etched module with that module.
    """
    equivalent = get_equivalent(module)
    if equivalent is not None:
        return equivalent
    for name, child in module.named_children():
        setattr(module, name, replace_modules(child))
    return module


def _get_constant(node: torch.Node) -> Union[None, torch.Tensor, int, float, bool, str]:
    assert (
        node.kind() == "prim::Constant"
    ), f"_get_constant called on node with kind {node.kind()}; must be prim::Constant"

    attr_names = node.attributeNames()
    if len(attr_names) == 0:
        return None
    else:
        assert (
            len(attr_names) == 1
        ), f"prim::Constant node has more than one attribute: {attr_names}"
        node_type = node.output().type().kind()
        if node_type == "BoolType":
            return node.i(attr_names[0]) != 0
        elif node_type == "DeviceObjType":
            return node.s(attr_names[0])
        elif node_type == "FloatType":
            return node.f(attr_names[0])
        elif node_type == "IntType":
            return node.i(attr_names[0])
        elif node_type == "StringType":
            return node.s(attr_names[0])
        elif node_type == "TensorType":
            # This a hack to get around a bug in torch.fx: https://github.com/pytorch/pytorch/issues/73992
            try:
                return node.t(attr_names[0]).item()
            except RuntimeError:
                return node.t(attr_names[0])
        else:
            raise NotImplementedError(f"Unsupported constant type: {node_type}")


def _get_attr_name(node: torch.Node) -> str:
    assert (
        node.kind() == "prim::GetAttr"
    ), f"_get_attr_name called on node with kind {node.kind()}; must be prim::GetAttr"
    assert node.attributeNames() == [
        "name"
    ], f"prim::GetAttr node has attributes other than 'name': {node.attributeNames()}"
    return node.s("name")


def _get_attr_full_name(node: torch.Node) -> str:
    full_name = _get_attr_name(node)

    curr_node = node
    while True:
        inputs = list(curr_node.inputs())
        assert len(inputs) == 1, f"curr_node has more than one input: {inputs}"
        curr_node = inputs[0].node()
        if curr_node.kind() != "prim::GetAttr":
            break
        full_name = _get_attr_name(curr_node) + ("." + full_name if full_name else "")
    return full_name


def _inputs_to_fx_nodes(
    inputs: List[torch.Value],
    fx_graph: fx.Graph,
    env: Dict[torch.Node, Tuple[fx.node.Argument, ...]],
) -> List[Union[fx.Node, fx.node.BaseArgumentTypes]]:
    fx_inputs: List[Union[fx.Node, fx.node.BaseArgumentTypes]] = []
    for inp in inputs:
        if inp.node() not in env:
            assert (
                inp.node().kind() == "prim::Param"
            ), f"Input node {inp.node()} is not a prim::Param but is instead a {inp.node().kind()}"
            env[inp.node()] = tuple(
                fx_graph.placeholder(name=_get_unique_name(inp.debugName()))
                for _ in range(inp.node().outputsSize())
            )
            assert (
                inp.offset() != 0
            ), f"Input node {inp.node()} has offset, implying a reference to `self`"
        fx_inputs.append(env[inp.node()][inp.offset()])
    return fx_inputs


def print_graph(graph: fx.Graph, message: str = "", verbosity: int = 0) -> None:
    if verbosity > 0:
        print(f"{message}: {len(graph.nodes)} nodes")
        if verbosity > 1:
            graph.print_tabular()


def compile(
    func: nn.Module, example_input: torch.Tensor, verbosity: int = 0
) -> SohuModule:
    start = time.time()
    # Replace all the modules with known replacements
    func = replace_modules(func).to(device=example_input.device)

    # Compile the function
    script = torch.jit.trace(func, example_input)
    assert isinstance(
        script, nn.Module
    ), f"torch.jit.trace returned a {type(script)} instead of a nn.Module"
    graph = script.graph.copy()  # type: ignore[assignment]
    assert isinstance(
        graph, torch.Graph
    ), f"torch.jit.trace(func, example_input).graph is a {type(graph)} instead of a torch.Graph"

    # Unfold function calls
    torch._C._jit_pass_onnx_function_substitution(graph)  # type: ignore[attr-defined] # TODO: I feel uncomfortable relying on a private API, this should be replaced at some point

    # Construct a torch.fx.GraphModule from the graph
    func_dict = function_replacements()
    fx_graph = SohuGraph()
    env: Dict[torch.Node, Tuple[fx.node.Argument, ...]] = {}
    fx_state_dict: Dict[str, Any] = {}
    for node in graph.nodes():
        kind = node.kind()
        inputs = list(node.inputs())
        # Inplace operations are treated the same as their non-inplace counterparts
        if kind[-1] == "_":
            kind = kind[:-1]
        if kind == "prim::Constant":
            fx_node = _get_constant(node)
        elif kind == "prim::GetAttr":
            attr_name = _get_attr_full_name(node)
            fx_state_dict[attr_name] = recursive_getattr(script, attr_name)
            fx_node = fx_graph.get_attr(attr_name)
        elif kind == "prim::ListUnpack":
            assert (
                len(inputs) == 1
            ), f"prim::ListUnpack node has more than one input: {inputs}"
            inp = inputs[0]
            fx_nodes: List[fx.Node] = []
            for i in range(node.outputsSize()):
                the_function = (
                    lambda x, i=i: x[0][i]
                    if hasattr(x[0], "__len__") and len(x[0]) > i
                    else never()
                )
                the_function.__name__ = f"getitem_{i}"
                fx_nodes.append(
                    fx_graph.call_function(
                        the_function=the_function,
                        args=(env[inp.node()],),
                    )
                )

            fx_node = tuple(fx_nodes)
        elif kind in func_dict:
            fx_node = fx_graph.call_function(
                the_function=func_dict[kind],
                args=tuple(_inputs_to_fx_nodes(inputs, fx_graph, env)),
            )
        else:
            raise NotImplementedError(f"Unsupported node kind: {kind}")
        env[node] = fx_node if isinstance(fx_node, tuple) else (fx_node,)
    assert (
        graph.return_node().kind() == "prim::Return"
        and len(list(graph.return_node().inputs())) == 1
    )
    fx_graph.output(env[graph.return_node().inputs().__next__().node()][0])
    fx_graph.lint()
    print_graph(fx_graph, "Initial graph", verbosity)

    fx_graph.eliminate_dead_code()  # While eliminate_dead_code is in transformations, this needs to be called here for fx_module to be constructable
    print_graph(fx_graph, "After eliminating dead code", verbosity)

    fx_module = SohuModule(fx_state_dict, fx_graph)
    # Apply graph transformations
    transformations = graph_transformations()
    any_change = True
    while any_change:
        any_change = False
        for transformation in transformations:
            changed = transformation(fx_module)
            any_change |= changed
            if changed:
                fx_graph.lint()
                print_graph(
                    fx_graph,
                    f"Applying transformation {transformation.__name__}",
                    verbosity,
                )
                fx_module.recompile()

    if verbosity > 0:
        print(f"Compilation took {time.time() - start} seconds")
    return fx_module
