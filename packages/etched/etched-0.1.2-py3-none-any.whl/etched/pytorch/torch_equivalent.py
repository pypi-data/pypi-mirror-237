import torch
import torch.nn as nn
import torch.nn.functional as F
from typing_extensions import Callable, Dict, List, Optional, Set, Tuple, Union


class Module(nn.Module):
    def post_load_state_dict(self):
        for _, module in self.named_children():
            if isinstance(module, Module):
                module.post_load_state_dict()


# Identity functions


def identity(input: torch.Tensor) -> torch.Tensor:
    return input


def dropout(input: torch.Tensor, p: float, training: bool) -> torch.Tensor:
    """
    Sohu only supports inference, so dropout is a no-op.
    """
    return input


# Binary ops


def add(
    input: torch.Tensor, other: torch.Tensor, alpha: Optional[Union[int, float, bool]]
) -> torch.Tensor:
    """
    Version of torch.add with no default arguments. Returns input + other * alpha.
    """
    return torch.add(input=input, other=other, alpha=alpha)


def mul(input: torch.Tensor, other: torch.Tensor) -> torch.Tensor:
    """
    Version of torch.mul with no default arguments. Returns input * other.
    """
    return torch.mul(input=input, other=other)


# Matmuls


class Linear(Module, nn.Linear):
    pass


def linear(
    input: torch.Tensor, weight: torch.Tensor, bias: Optional[torch.Tensor]
) -> torch.Tensor:
    """
    Linear layer with no default arguments.
    """
    return F.linear(input=input, weight=weight, bias=bias)


def baddbmm(
    input: torch.Tensor,
    batch1: torch.Tensor,
    batch2: torch.Tensor,
    beta: float,
    alpha: float,
) -> torch.Tensor:
    """
    Batched matrix multiplication accumulation with no default arguments. Returns beta * input + alpha * (batch1 @ batch2).
    """
    return torch.baddbmm(
        input=input, batch1=batch1, batch2=batch2, beta=beta, alpha=alpha, out=None
    )


def bmm(input: torch.Tensor, mat2: torch.Tensor) -> torch.Tensor:
    """
    Batched matrix multiplication with no default arguments. Returns input @ mat2.
    """
    return torch.bmm(input=input, mat2=mat2)


# Attention


class ScaledDotProductAttention(Module):
    pass


def scaled_dot_product_attention(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attn_mask: Optional[torch.Tensor],
    dropout_p: float,
    is_causal: bool,
) -> torch.Tensor:
    """
    Scaled dot product attention with no default arguments.
    """
    return F.scaled_dot_product_attention(
        query=query,
        key=key,
        value=value,
        attn_mask=attn_mask,
        dropout_p=dropout_p,
        is_causal=is_causal,
    )


# Norms


class LayerNorm(Module, nn.LayerNorm):
    pass


def layer_norm(
    input: torch.Tensor,
    normalized_shape: Tuple[int, ...],
    weight: Optional[torch.Tensor],
    bias: Optional[torch.Tensor],
    eps: float,
    ignored: bool,
) -> torch.Tensor:
    """
    Layer normalization which only normalizes along the last dimension, no default arguments, and which takes an extra dummy argument.
    """
    return F.layer_norm(
        input=input,
        normalized_shape=normalized_shape,
        weight=weight,
        bias=bias,
        eps=eps,
    )


def softmax(input: torch.Tensor, dim: Optional[int], unknown: None) -> torch.Tensor:
    assert unknown is None
    return F.softmax(input=input, dim=dim)


def log_softmax(input: torch.Tensor, dim: Optional[int], unknown: None) -> torch.Tensor:
    """
    Log softmax with no default arguments.
    """
    assert unknown is None
    return F.log_softmax(input=input, dim=dim)


def get_supported_norms() -> Set[Callable[..., torch.Tensor]]:
    """
    Returns a dictionary whose keys are norms that can be run on Sohu.
    """
    return {layer_norm}


# Activation functions


class ReLU(Module, nn.ReLU):
    pass


def relu(input: torch.Tensor) -> torch.Tensor:
    """
    ReLU activation function with no default arguments.
    """
    return F.relu(input=input)


class GELU(Module, nn.GELU):
    pass


def gelu(input: torch.Tensor, approximate: str) -> torch.Tensor:
    """
    Gaussian Error Linear Unit (GELU) activation function which can accept `approximate` as a positional argument and with no default arguments.
    """
    return F.gelu(input=input, approximate=approximate)


class SiLU(Module, nn.SiLU):
    pass


def silu(input: torch.Tensor) -> torch.Tensor:
    """
    Sigmoid Linear Unit (SiLU) activation function with no default arguments.
    """
    return F.silu(input=input)


# Reshapes


def flatten(input: torch.Tensor, start_dim: int, end_dim: int) -> torch.Tensor:
    """
    Flatten function with no default arguments.
    """
    return torch.flatten(input=input, start_dim=start_dim, end_dim=end_dim)


def listContruct(*args) -> tuple:
    return args


def size(input: torch.Tensor, dim: int) -> int:
    """
    Returns the size of the input tensor along the specified dimension.
    """
    return input.size(dim)


def split(
    tensor: torch.Tensor, split_size_or_sections: Union[int, List[int]], dim: int
) -> Tuple[torch.Tensor, ...]:
    return torch.split(
        tensor=tensor, split_size_or_sections=split_size_or_sections, dim=dim
    )


def numToTensor(num: int) -> torch.Tensor:
    """
    Converts a number to a tensor.
    """
    return torch.tensor(num)


def permute(input: torch.Tensor, dims: torch.Size) -> torch.Tensor:
    return torch.permute(input=input, dims=dims)


def tensorToInt(input: torch.Tensor) -> int:
    """
    Converts a tensor to an int.
    """
    output = input.item()
    assert isinstance(output, int)
    return output


def transpose(input: torch.Tensor, dim0: int, dim1: int) -> torch.Tensor:
    return torch.transpose(input=input, dim0=dim0, dim1=dim1)


def triu(input: torch.Tensor, diagonal: int) -> torch.Tensor:
    return torch.triu(input=input, diagonal=diagonal)


def view(input: torch.Tensor, size: torch.Size) -> torch.Tensor:
    """
    Reshapes the input tensor to the specified shape. We don't care about contiguity in the IR, so we use reshape instead of view.
    """
    return input.reshape(size)


# Fillers


def ones(
    size: torch.Size,
    ignore: int,
    dtype: Optional[torch.dtype],
    device: Optional[torch.device],
    requires_grad: bool,
) -> torch.Tensor:
    return torch.ones(
        size=size, dtype=dtype, device=device, requires_grad=requires_grad
    )


def zeros(
    size: torch.Size,
    ignore: int,
    dtype: Optional[torch.dtype],
    device: Optional[torch.device],
    requires_grad: bool,
) -> torch.Tensor:
    return torch.zeros(
        size=size, dtype=dtype, device=device, requires_grad=requires_grad
    )


def function_replacements() -> Dict[str, Callable]:
    return {
        "prim::ListConstruct": listContruct,
        "prim::NumToTensor": numToTensor,
        "aten::add": add,
        "aten::baddbmm": baddbmm,
        "aten::bmm": bmm,
        "aten::contiguous": lambda x, y: x.contiguous(y),
        "aten::dropout": dropout,
        "aten::empty": torch.empty,
        "aten::flatten": flatten,
        "aten::gelu": gelu,
        "aten::Int": tensorToInt,
        "aten::layer_norm": layer_norm,
        "aten::linear": linear,
        "aten::mul": mul,
        "aten::log_softmax": log_softmax,
        "aten::ones": ones,
        "aten::permute": permute,
        "aten::relu": relu,
        "aten::reshape": view,
        "aten::scaled_dot_product_attention": F.scaled_dot_product_attention,
        "aten::silu": silu,
        "aten::size": size,
        "aten::softmax": softmax,
        "aten::split": split,
        "aten::transpose": transpose,
        "aten::triu": triu,
        "aten::view": view,
        "aten::zeros": zeros,
    }
