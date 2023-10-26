import torch
import torch.fx as fx
from typing_extensions import Callable, Dict, Hashable, List, Set, Tuple

from .func_groups import commutative_funcs, get_no_ops, linear_funcs
from .iir import (
    generate_causal_mask,
    get_causal_attention_scores,
    get_k,
    get_q,
    get_qkT,
    get_v,
    merge_dims,
    qkv_split,
)
from .module import SohuGraph, SohuModule
from .torch_equivalent import (
    add,
    baddbmm,
    bmm,
    listContruct,
    mul,
    numToTensor,
    ones,
    size,
    softmax,
    split,
    tensorToInt,
    transpose,
    triu,
    view,
)
from .utils import Universe, item


def decompose_baddbmm(module: fx.GraphModule) -> bool:
    graph = module.graph
    changed = False
    for node in graph.nodes:
        assert isinstance(node, fx.Node)
        if node.target == baddbmm:
            with graph.inserting_before(node):
                matmul_node = graph.call_function(
                    the_function=bmm,
                    args=(node.args[1], node.args[2]),
                )
                alpha_mul_node = graph.call_function(
                    the_function=mul,
                    args=(matmul_node, node.args[4]),
                )
                add_node = graph.call_function(
                    the_function=add,
                    args=(alpha_mul_node, node.args[0], node.args[3]),
                )
            node.replace_all_uses_with(add_node)
            changed = True
    return changed


def eliminate_dead_code(module: fx.GraphModule) -> bool:
    return module.graph.eliminate_dead_code()


def eliminate_unused_inputs(module: fx.GraphModule) -> bool:
    graph = module.graph
    changed = False
    for node in graph.nodes:
        assert isinstance(node, fx.Node)
        if node.op == "placeholder" and len(node.users) == 0:
            node.graph.erase_node(node)
            changed = True
    return changed


def num_nonattr_inputs(node: fx.Node) -> int:
    return len([inp for inp in node.all_input_nodes if inp.op != "get_attr"])


def num_users(node: fx.Node) -> int:
    return len(node.users)


def nonnode_args(node: fx.Node) -> Tuple:
    return tuple(arg for arg in node.args if not isinstance(arg, fx.Node))


def get_sequential_subgraphs(
    graph: fx.Graph, min_length: int = 2, allowed_funcs: Set[Callable] = Universe()
) -> List[Tuple[fx.Node, int]]:
    """
    Finds all the maximal sequential subgraphs in the graph, and returns them as a list of tuples, where the first element of each tuple is the first node in the corresponding subgraph, and the second element is the number of nodes in that subgraph.
    """
    subgraphs: List[Tuple[fx.Node, int]] = []
    used_nodes: Set[fx.Node] = set()
    for node in graph.nodes:
        if node in used_nodes:
            continue
        assert isinstance(node, fx.Node)
        curr_node = node
        subgraph = (node, 0)
        while (
            curr_node.op == "call_function"
            and num_nonattr_inputs(curr_node) == 1
            and num_users(curr_node) == 1
            and curr_node.target in allowed_funcs
        ):
            subgraph = (subgraph[0], subgraph[1] + 1)
            curr_node = list(curr_node.users)[0]
            used_nodes.add(curr_node)
        if subgraph[1] >= min_length:
            subgraphs.append(subgraph)
    return subgraphs


def fuse_sequential_subgraphs(graph: fx.Graph) -> bool:
    sequential_subgraphs = get_sequential_subgraphs(graph)

    raise NotImplementedError()


def remove_add_zero(module: fx.GraphModule) -> bool:
    graph = module.graph
    changed = False
    for node in graph.nodes:
        assert isinstance(node, fx.Node)
        if node.target == add and 0.0 in node.args:
            if node.args[0] == 0.0:
                node.target = mul
                node.args = (node.args[1], node.args[2])
            elif isinstance(node.args[0], fx.Node):
                node.replace_all_uses_with(node.args[0])
            else:
                continue
            changed = True
    return changed


def remove_identity(module: fx.GraphModule) -> bool:
    """
    Removes identity nodes from the graph.
    """
    graph = module.graph
    changed = False
    no_ops = get_no_ops()
    for node in graph.nodes:
        assert isinstance(node, fx.Node)
        if (
            node.op == "call_function"
            and node.target in no_ops
            and isinstance(replacement := node.args[no_ops[node.target]], fx.Node)
        ):
            node.replace_all_uses_with(replacement)
            changed = True
    return changed


def fuse_causal_mask_generation(module: fx.GraphModule) -> bool:
    graph = module.graph
    changed = False
    for node in graph.nodes:
        assert isinstance(node, fx.Node)
        if (
            node.target == ones
            and num_users(node) == 1
            and (mul_node := list(node.users)[0]).target == mul
            and mul_node.args == (node, -torch.inf)
            and num_users(mul_node) == 1
            and (triu_node := list(mul_node.users)[0]).target == triu
        ):
            with graph.inserting_after(triu_node):
                new_node = graph.call_function(
                    the_function=generate_causal_mask,
                    args=node.args,
                    kwargs={"diagonal": triu_node.args[1]},
                )
            triu_node.replace_all_uses_with(new_node)
            changed = True
    return changed


def fuse_get_qkT(module: SohuModule) -> bool:
    changed = False
    graph = module.graph
    assert isinstance(graph, SohuGraph)
    for node in module.nodes():
        if (
            node.target == view
            and isinstance(bmm_node := node.args[0], fx.Node)
            and bmm_node.target == bmm
            and isinstance(transpose_q_node := bmm_node.args[0], fx.Node)
            and transpose_q_node.target == transpose
            and transpose_q_node.args[1:] == (0, 1)
            and isinstance(merge_q_node := transpose_q_node.args[0], fx.Node)
            and merge_q_node.target == merge_dims
            and merge_q_node.kwargs["dims"] == (1, 2)
            and isinstance(q_node := item(merge_q_node.args), fx.Node)
            and q_node.target == get_q
            and isinstance(transpose_k_node1 := bmm_node.args[1], fx.Node)
            and transpose_k_node1.target == transpose
            and transpose_k_node1.args[1:] == (1, 2)
            and isinstance(transpose_k_node0 := transpose_k_node1.args[0], fx.Node)
            and transpose_k_node0.target == transpose
            and transpose_k_node0.args[1:] == (0, 1)
            and isinstance(merge_k_node := transpose_k_node0.args[0], fx.Node)
            and merge_k_node.target == merge_dims
            and merge_k_node.kwargs["dims"] == (1, 2)
            and isinstance(k_node := item(merge_k_node.args), fx.Node)
            and k_node.target == get_k
            and q_node.args == k_node.args
            and q_node.kwargs["num_heads"] == k_node.kwargs["num_heads"]
            and isinstance(list_node := node.args[1], fx.Node)
            and list_node.target == listContruct
            and len(list_node.args) == 4
            and isinstance(size1_node := list_node.args[0], fx.Node)
            and size1_node.target == size
            and size1_node.args[1] == 1
            and size1_node.args[0] in graph.aligned_nodes
            and isinstance(size2_node := list_node.args[1], fx.Node)
            and size2_node.target == size
            and size2_node.args[1] == 2
            and size2_node.args[0] in {q_node, k_node}
            and isinstance(size0_node := list_node.args[2], fx.Node)
            and size0_node.target == size
            and size0_node.args[1] == 0
            and size0_node.args[0] in graph.aligned_nodes
            and size0_node == list_node.args[3]
        ):
            with graph.inserting_before(node):
                q_scale = q_node.kwargs["scale"]
                k_scale = k_node.kwargs["scale"]
                assert isinstance(q_scale, (int, float)) and isinstance(
                    k_scale, (int, float)
                )
                new_node = graph.call_function(
                    the_function=get_qkT,
                    args=q_node.args,
                    kwargs={
                        "num_heads": q_node.kwargs["num_heads"],
                        "scale": q_scale * k_scale,
                    },
                )
            node.replace_all_uses_with(new_node)
            changed = True
    return changed


def fuse_get_causal_attention_scores(module: SohuModule) -> bool:
    changed = False
    for node in module.nodes():
        if (
            node.target == softmax
            and isinstance(add_node := node.args[0], fx.Node)
            and add_node.target == add
            and isinstance(inp0 := add_node.args[0], fx.Node)
            and isinstance(inp1 := add_node.args[1], fx.Node)
            and {inp0.target, inp1.target} == {generate_causal_mask, get_qkT}
            # TODO: Add arg to make sure dimensions match
            and node.args[1] == -1
            and node.args[2] is None
        ):
            with module.graph.inserting_before(node):
                qkT_node = inp0 if inp0.target == get_qkT else inp1
                new_node = module.graph.call_function(
                    the_function=get_causal_attention_scores,
                    args=qkT_node.args,
                    kwargs=qkT_node.kwargs,
                )
            node.replace_all_uses_with(new_node)
            changed = True
    return changed


def fuse_merge_first_dims(module: SohuModule) -> bool:
    graph = module.graph
    assert isinstance(graph, SohuGraph)
    changed = False
    for node in module.nodes():
        if (
            node.target == view
            and isinstance(list_node := node.args[1], fx.Node)
            and list_node.target == listContruct
            and len(list_node.args) == 3
            and isinstance(size0_node := list_node.args[1], fx.Node)
            and len(size0_node.args) == 2
            and size0_node.args[1] == 2
            and isinstance(size0_node.args[0], fx.Node)
            # and size0_node.args[0] in graph.aligned_nodes
            and isinstance(mul_node := list_node.args[0], fx.Node)
            and mul_node.target == mul
            and (
                (
                    isinstance(size1_node := mul_node.args[i:=0], fx.Node)
                    and size1_node.args[1] == 1
                )
                or (
                    isinstance(size1_node := mul_node.args[i:=1], fx.Node)
                    and size1_node.args[1] == 1
                )
            )
            # and size1_node.args[0] in graph.aligned_nodes
            and isinstance(size2_node := mul_node.args[1 - i], fx.Node)
            and size2_node.args[1] == 0
            # and size2_node.args[0] in graph.aligned_nodes
            and list_node.args[2] == -1
            and node.args[0] == size2_node.args[0]
        ):
            with graph.inserting_before(node):
                new_node = graph.call_function(
                    the_function=merge_dims,
                    args=(node.args[0],),
                    kwargs={"dims": (0, 1)},
                )
            node.replace_all_uses_with(new_node)
            changed = True
    return changed


def fuse_merge_middle_dims(module: SohuModule) -> bool:
    graph = module.graph
    assert isinstance(graph, SohuGraph)
    changed = False
    for node in module.nodes():
        if (
            node.target == view
            and isinstance(list_node := node.args[1], fx.Node)
            and list_node.target == listContruct
            and len(list_node.args) == 3
            and isinstance(size0_node := list_node.args[0], fx.Node)
            and len(size0_node.args) == 2
            and size0_node.args[1] == 0
            and isinstance(size0_node.args[0], fx.Node)
            # and size0_node.args[0] in graph.aligned_nodes
            and isinstance(mul_node := list_node.args[1], fx.Node)
            and mul_node.target == mul
            and (
                (
                    isinstance(size1_node := mul_node.args[i:=0], fx.Node)
                    and size1_node.args[1] == 1
                )
                or (
                    isinstance(size1_node := mul_node.args[i:=1], fx.Node)
                    and size1_node.args[1] == 1
                )
            )
            # and size1_node.args[0] in graph.aligned_nodes
            and isinstance(size2_node := mul_node.args[1 - i], fx.Node)
            and size2_node.args[1] == 2
            and size2_node.args[0] in graph.aligned_nodes
            and list_node.args[2] == -1
            and node.args[0] == size2_node.args[0]
        ):
            with graph.inserting_before(node):
                new_node = graph.call_function(
                    the_function=merge_dims,
                    args=(node.args[0],),
                    kwargs={"dims": (1, 2)},
                )
            node.replace_all_uses_with(new_node)
            changed = True
    return changed


def fuse_mul(module: fx.GraphModule) -> bool:
    graph = module.graph
    changed = False
    for node in graph.nodes:
        assert isinstance(node, fx.Node)
        if node.target == mul and (
            isinstance(node.args[i:=0], (int, float))
            or isinstance(node.args[i:=1], (int, float))
        ):
            for user in node.users.copy():
                if "scale" in user.kwargs and isinstance(
                    user.kwargs["scale"], (int, float)
                ):
                    kwargs = user.kwargs.copy()
                    assert isinstance(x := node.args[i], (int, float)) and isinstance(
                        scale := user.kwargs["scale"], (int, float)
                    )
                    kwargs["scale"] = x * scale
                    user.args = tuple(
                        arg if arg != node else node.args[1 - i] for arg in user.args
                    )
                    user.kwargs = {
                        key: (val if val != node else node.args[1 - i])
                        for key, val in kwargs.items()
                    }
                    changed = True
    return changed


def fuse_numToTensor_tensorToInt(module: fx.GraphModule) -> bool:
    graph = module.graph
    changed = False
    for node in graph.nodes:
        assert isinstance(node, fx.Node)
        if (
            node.op == "call_function"
            and len(node.users) >= 1
            and {node.target, (node2 := list(node.users)[0]).target}
            == {numToTensor, tensorToInt}
        ):
            if len(node.all_input_nodes) == 1:
                node2.replace_all_uses_with(node.all_input_nodes[0])
            else:
                assert (
                    not node.all_input_nodes
                ), f"{len(node.all_input_nodes)}) is too many for {node}"
                for user in list(node2.users):
                    user.args = tuple(
                        arg if arg != node2 else item(node.args) for arg in user.args
                    )

            changed = True
    return changed


def fuse_qkv_split(module: fx.GraphModule) -> bool:
    """
    Finds instances of a tensor being reshaped and split into three tensors, and replaces it with a call to qkv_split.
    """
    graph = module.graph
    changed = False
    for node in graph.nodes:
        assert isinstance(node, fx.Node)
        if (
            node.op == "call_function"
            and node.target == listContruct
            and len(node.all_input_nodes) == 2
            and (size_node0 := node.all_input_nodes[0]).all_input_nodes
            == (size_node1 := node.all_input_nodes[1]).all_input_nodes
            == (view_node := list(node.users)[0]).all_input_nodes[:1]
            and size_node0.target == size_node1.target == size
            and {nonnode_args(size_node0), nonnode_args(size_node1)} == {(0,), (1,)}
            and num_users(size_node0) == num_users(size_node1) == 1
            and len(nonnode_args(node)) == 2
            and len(view_node.all_input_nodes) == 2
            and view_node.target == view
            and len(view_node.all_input_nodes) == 2
            and num_users(view_node) == 1
            and (split_node := list(view_node.users)[0]).target == split
            and nonnode_args(split_node) == (nonnode_args(node)[0] / 3, -2)
        ):
            changed = True
            with graph.inserting_after(split_node):
                new_node = graph.call_function(
                    the_function=qkv_split,
                    args=(orig_node := size_node0.all_input_nodes[0],),
                    kwargs={"num_heads": nonnode_args(split_node)[0]},
                )
                for user in list(split_node.users):
                    if (
                        isinstance(user.target, Callable)
                        and user.target.__name__[:-1] == "getitem_"
                    ):
                        if user.target.__name__[-1] == "0":
                            q_node = graph.call_function(
                                the_function=get_q,
                                args=(orig_node,),
                                kwargs={
                                    "num_heads": nonnode_args(split_node)[0],
                                    "scale": 1,
                                },
                            )
                            user.replace_all_uses_with(q_node)
                        elif user.target.__name__[-1] == "1":
                            k_node = graph.call_function(
                                the_function=get_k,
                                args=(orig_node,),
                                kwargs={
                                    "num_heads": nonnode_args(split_node)[0],
                                    "scale": 1,
                                },
                            )
                            user.replace_all_uses_with(k_node)
                        elif user.target.__name__[-1] == "2":
                            v_node = graph.call_function(
                                the_function=get_v,
                                args=(orig_node,),
                                kwargs={"num_heads": nonnode_args(split_node)[0]},
                            )
                            user.replace_all_uses_with(v_node)
                        else:
                            continue
            split_node.replace_all_uses_with(new_node)
    return changed


def list_construct_to_constant(module: SohuModule) -> bool:
    changed = False
    for node in module.nodes():
        if node.target == listContruct and not node.all_input_nodes:
            for user in list(node.users):
                user.args = tuple(
                    arg if arg != node else node.args for arg in user.args
                )
                user.kwargs = {
                    key: (val if val != node else node.args)
                    for key, val in user.kwargs.items()
                }
            changed = True
    return changed


def is_commutative(node: fx.Node) -> bool:
    return node.target in commutative_funcs()


def hashable_node_repr(node: fx.Node) -> Hashable:
    """
    Generates a hashable representation of a node, such that any two nodes with the same representation compute the same result.
    """
    ret = (
        node.op,
        node.target,
        tuple(sorted(node.args, key=lambda arg: hash(arg)))
        if is_commutative(node)
        else node.args,
        tuple(sorted(node.kwargs.items())),
    )
    if (
        node.target == size
        and node.args[1] in {0, 1}
        and isinstance(node.args[0], fx.Node)
        and isinstance(node.args[0].graph, SohuGraph)
        and node.args[0] in node.args[0].graph.aligned_nodes
    ):
        ret = (size, node.args[1])
    hash(ret)
    return ret


def merge_identical_nodes(module: SohuModule) -> bool:
    changed = False
    distinct_nodes: Dict[Hashable, fx.Node] = {}
    for node in module.nodes():
        node_repr = hashable_node_repr(node)
        if node_repr in distinct_nodes:
            node.replace_all_uses_with(distinct_nodes[node_repr])
            changed = True
        else:
            distinct_nodes[node_repr] = node
    return changed


def slide_mul_nodes(module: fx.GraphModule) -> bool:
    """
    If a mul node is being applied to a linear node, it is instead applied to the input of that node.
    """
    graph = module.graph
    changed = False
    linears = linear_funcs()
    for j, node in enumerate(graph.nodes.__reversed__()):
        assert isinstance(node, fx.Node)
        if node.target == mul:
            while (
                isinstance(inp := node.args[i:=0], fx.Node) and inp.target in linears
            ) or (
                isinstance(inp := node.args[i:=1], fx.Node) and inp.target in linears
            ):
                with graph.inserting_before(inp):
                    new_node = graph.call_function(
                        the_function=mul,
                        args=(
                            inp.args[index := next(iter(linears[inp.target]))],
                            node.args[1 - i],
                        ),
                    )
                new_args = list(inp.args)
                new_args[index] = new_node
                inp.args = tuple(new_args)
                node.replace_all_uses_with(inp)
                graph.erase_node(node)
                node = new_node
                changed = True
    return changed


def graph_transformations() -> List[Callable[[SohuModule], bool]]:
    """
    Returns a list of graph transformations which modify the graph of a GraphModule in-place and return whether the graph was modified. It is *not* guaranteed that the module will be recompiled if the graph is modified.
    """
    return [
        decompose_baddbmm,
        eliminate_dead_code,
        eliminate_unused_inputs,
        remove_add_zero,
        remove_identity,
        fuse_causal_mask_generation,
        fuse_get_qkT,
        fuse_get_causal_attention_scores,
        fuse_merge_first_dims,
        fuse_merge_middle_dims,
        fuse_mul,
        fuse_numToTensor_tensorToInt,
        fuse_qkv_split,
        list_construct_to_constant,
        merge_identical_nodes,
        slide_mul_nodes,
    ]
