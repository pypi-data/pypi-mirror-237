"""
Intermediate IR functions, which neither correspond to PyTorch functions nor appear in the final IR.
"""

import torch
import torch.nn.functional as F
from typing_extensions import Tuple

from .torch_equivalent import ones


def generate_causal_mask(
    *args,
    diagonal: int = 0,
) -> torch.Tensor:
    return torch.triu(
        -torch.inf * ones(*args),
        diagonal=diagonal,
    )


def qkv_split(
    x: torch.Tensor, *, num_heads: int
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Splits the input tensor into equally sized query, key, and value tensors.
    """
    batch_size, seq_len, hidden_size = x.shape
    head_size = hidden_size // (3 * num_heads)
    x = x.reshape(batch_size, seq_len, 3 * num_heads, head_size)
    q, k, v = torch.split(x, [num_heads, num_heads, num_heads], dim=-2)
    return q, k, v


def get_q(x: torch.Tensor, *, num_heads: int, scale: float) -> torch.Tensor:
    batch_size, seq_len, hidden_size = x.shape
    head_size = hidden_size // (3 * num_heads)
    x = x.reshape(batch_size, seq_len, 3 * num_heads, head_size)
    q = x[:, :, :num_heads, :]
    return q * scale


def get_k(x: torch.Tensor, *, num_heads: int, scale: float) -> torch.Tensor:
    batch_size, seq_len, hidden_size = x.shape
    head_size = hidden_size // (3 * num_heads)
    x = x.reshape(batch_size, seq_len, 3 * num_heads, head_size)
    k = x[:, :, num_heads : 2 * num_heads, :]
    return k * scale


def get_v(x: torch.Tensor, *, num_heads: int) -> torch.Tensor:
    batch_size, seq_len, hidden_size = x.shape
    head_size = hidden_size // (3 * num_heads)
    x = x.reshape(batch_size, seq_len, 3 * num_heads, head_size)
    v = x[:, :, 2 * num_heads :, :]
    return v


def get_qkT(x: torch.Tensor, *, num_heads: int, scale: float) -> torch.Tensor:
    q, k = get_q(x, num_heads=num_heads, scale=1), get_k(
        x, num_heads=num_heads, scale=1
    )
    return torch.matmul(q, k.transpose(-1, -2)) * scale


def get_causal_attention_scores(x: torch.Tensor, *, num_heads: int, scale: float):
    _, seqlen, _ = x.shape
    qkT = get_qkT(x, num_heads=num_heads, scale=scale)
    masked_qkT = qkT + torch.triu(
        torch.ones(
            (seqlen, seqlen),
            dtype=qkT.dtype,
            device=qkT.device,
        )
        * float("-inf"),
        diagonal=1,
    )
    return F.softmax(masked_qkT, dim=-1)


def merge_dims(x: torch.Tensor, *, dims: Tuple[int, int]) -> torch.Tensor:
    assert abs(dims[0] - dims[1]) == 1
    new_shape = list(x.shape)
    new_shape[dims[0]] *= new_shape.pop(dims[1])
    return x.reshape(*new_shape)
