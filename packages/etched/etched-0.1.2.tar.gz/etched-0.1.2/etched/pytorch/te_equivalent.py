import math

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing_extensions import List, Literal, Optional, Tuple, Union

from .torch_equivalent import GELU, LayerNorm, Module, ReLU
from .utils import never

ActivationStr = Literal["gelu", "geglu", "relu", "reglu", "squared_relu", "swiglu"]


class Linear(Module):
    def __init__(
        self,
        in_features: int,
        out_features: int,
        bias: bool = True,
        params_dtype: torch.dtype = torch.float32,
        parameters_split: Optional[Tuple[str, ...]] = None,
    ):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.use_bias = bias
        self.params_dtype = params_dtype
        self.parameters_split = (
            parameters_split if parameters_split is not None else ("",)
        )

        self.register_buffer(
            "weight_tensor",
            torch.empty(self.out_features, self.in_features, dtype=params_dtype),
            persistent=False,
        )
        if self.use_bias:
            self.register_buffer(
                "bias_tensor",
                torch.empty(self.out_features, dtype=params_dtype),
                persistent=False,
            )
        else:
            self.register_buffer(
                "bias_tensor", torch.Tensor().to(dtype=params_dtype), persistent=False
            )

        assert isinstance(self.weight_tensor, torch.Tensor)
        assert isinstance(self.bias_tensor, torch.Tensor)

        split_size = self.out_features // len(self.parameters_split)

        self.weight_names: List[str] = []
        self.bias_names: List[str] = []

        for i, pname in enumerate(self.parameters_split):
            wname = pname + "weight"
            bname = pname + "bias"

            self.register_parameter(
                wname,
                nn.Parameter(self.weight_tensor[i * split_size : (i + 1) * split_size]),
            )

            if self.use_bias:
                self.register_parameter(
                    bname,
                    nn.Parameter(
                        self.bias_tensor[i * split_size : (i + 1) * split_size]
                    ),
                )
            else:
                self.register_buffer(
                    bname, torch.Tensor().to(dtype=params_dtype), persistent=False
                )

            self.weight_names.append(wname)
            self.bias_names.append(bname)

    def post_load_state_dict(self):
        super().post_load_state_dict()
        self.weight_tensor = torch.cat(
            [getattr(self, wname) for wname in self.weight_names], dim=0
        )
        self.bias_tensor = torch.cat(
            [getattr(self, bname) for bname in self.bias_names], dim=0
        )

    def forward(self, inp: torch.Tensor) -> torch.Tensor:
        bias_tensor = self.bias_tensor
        weight_tensor = self.weight_tensor

        assert isinstance(bias_tensor, torch.Tensor)
        assert isinstance(weight_tensor, torch.Tensor)

        return F.linear(
            inp, weight=weight_tensor, bias=bias_tensor if self.use_bias else None
        )


class LayerNormLinear(Module):
    def __init__(
        self,
        in_features: int,
        out_features: int,
        eps: float = 1e-5,
        bias: bool = True,
        parameters_split: Optional[Tuple[str, ...]] = None,
        params_dtype: torch.dtype = torch.float32,
    ):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.eps = eps
        self.use_bias = bias
        self.parameters_split = (
            parameters_split if parameters_split is not None else ("",)
        )

        self.layer_norm_weight = nn.Parameter(
            torch.empty(in_features, dtype=params_dtype)
        )
        self.layer_norm_bias = nn.Parameter(
            torch.empty(in_features, dtype=params_dtype)
        )

        self.weight_tensor = nn.Parameter(
            torch.empty(out_features, in_features, dtype=params_dtype)
        )
        self.bias_tensor = nn.Parameter(torch.empty(out_features, dtype=params_dtype))

        self.weight_names: List[str] = []
        self.bias_names: List[str] = []

        split_size = self.out_features // len(self.parameters_split)
        for i, pname in enumerate(self.parameters_split):
            wname = pname + "weight"
            bname = pname + "bias"

            self.register_parameter(
                wname,
                nn.Parameter(self.weight_tensor[i * split_size : (i + 1) * split_size]),
            )

            self.weight_names.append(wname)

            self.register_parameter(
                bname,
                nn.Parameter(self.bias_tensor[i * split_size : (i + 1) * split_size])
                if self.use_bias
                else None,
            )

            self.bias_names.append(bname)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        ln_x = F.layer_norm(
            x,
            normalized_shape=(self.in_features,),
            weight=self.layer_norm_weight,
            bias=self.layer_norm_bias,
            eps=self.eps,
        )

        fc_x = F.linear(
            ln_x, self.weight_tensor, self.bias_tensor if self.use_bias else None
        )
        return fc_x

    def post_load_state_dict(self):
        super().post_load_state_dict()
        self.weight_tensor = nn.Parameter(
            torch.cat([getattr(self, wname) for wname in self.weight_names], dim=0)
        )
        self.bias_tensor = nn.Parameter(
            torch.cat(
                [
                    getattr(self, bname)
                    for bname in self.bias_names
                    if getattr(self, bname) is not None
                ]
                or [self.bias_tensor],
                dim=0,
            )
        )


class LayerNormMLP(Module):
    def __init__(
        self,
        hidden_size: int,
        ffn_hidden_size: int,
        eps: float = 1e-5,
        bias: bool = True,
        normalization: Literal["LayerNorm", "RMSNorm"] = "LayerNorm",
        activation: str = "gelu",
    ):
        super().__init__()
        self.hidden_size = hidden_size
        self.ffn_hidden_size = ffn_hidden_size
        self.eps = eps
        self.use_bias = bias
        self.normalization = normalization
        self.activation = activation

        self.layer_norm_weight = nn.Parameter(torch.Tensor(hidden_size))
        self.layer_norm_bias = nn.Parameter(torch.Tensor(hidden_size))
        self.fc1_weight = nn.Parameter(torch.Tensor(ffn_hidden_size, hidden_size))
        self.fc2_weight = nn.Parameter(torch.Tensor(hidden_size, ffn_hidden_size))
        if bias:
            self.fc1_bias = nn.Parameter(torch.Tensor(ffn_hidden_size))
            self.fc2_bias = nn.Parameter(torch.Tensor(hidden_size))
        else:
            self.register_parameter("fc1_bias", None)
            self.register_parameter("fc2_bias", None)

        assert activation in [
            "gelu",
            "geglu",
            "relu",
            "reglu",
            "squared_relu",
            "swiglu",
        ]
        self.activation_func = (
            ReLU()
            if activation == "relu"
            else GELU()
            if activation == "gelu"
            else never()
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        ln_x = F.layer_norm(
            x,
            normalized_shape=(self.hidden_size,),
            weight=self.layer_norm_weight,
            bias=self.layer_norm_bias,
            eps=self.eps,
        )
        fc1_x = F.linear(ln_x, self.fc1_weight, self.fc1_bias)

        act_x = self.activation_func(fc1_x)

        fc2_x = F.linear(act_x, self.fc2_weight, self.fc2_bias)
        return fc2_x


class DotProductAttention(Module):
    """
    Replacement for te.attention.DotProductAttention
    """

    def __init__(
        self,
        num_attention_heads: int,
        kv_channels: int,
        num_gqa_groups: Optional[int] = None,
        attn_mask_type: str = "causal",
        attention_type: str = "self",
    ):
        super().__init__()
        self.num_attention_heads = num_attention_heads
        self.kv_channels = kv_channels
        self.num_gqa_groups = num_gqa_groups
        self.attn_mask_type = attn_mask_type
        self.attention_type = attention_type

    def forward(
        self,
        query_layer: torch.Tensor,
        key_layer: torch.Tensor,
        value_layer: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        batch_size, seqlen = query_layer.shape[1], query_layer.shape[0]

        # [b, np, sq, sk]
        output_size = (
            query_layer.size(1),
            query_layer.size(2),
            query_layer.size(0),
            key_layer.size(0),
        )

        # [sq, b, np, hn] -> [sq, b * np, hn]
        query_layer = query_layer.reshape(
            query_layer.size(0), query_layer.size(1) * query_layer.size(2), -1
        )
        # [sk, b, np, hn] -> [sk, b * np, hn]
        key_layer = key_layer.reshape(
            key_layer.size(0), key_layer.size(1) * key_layer.size(2), -1
        )

        # preallocting result tensor: [b * np, sq, sk]
        matmul_result = torch.zeros(
            (output_size[0] * output_size[1], output_size[2], output_size[3]),
            dtype=query_layer.dtype,
            device=query_layer.device,
        )

        scale = math.sqrt(self.kv_channels)

        # Raw attention scores. [b * np, sq, sk]
        matmul_result = torch.baddbmm(
            matmul_result,
            query_layer.transpose(0, 1),  # [b * np, sq, hn]
            key_layer.transpose(0, 1).transpose(1, 2),  # [b * np, hn, sk]
            beta=0.0,
            alpha=(1.0 / scale),
        )

        # change view to [b, np, sq, sk]
        attention_scores = matmul_result.reshape(*output_size)

        if attention_mask is not None:
            attention_scores += attention_mask
        elif self.attn_mask_type == "causal" and self.attention_type == "self":
            # causal mask
            attention_scores += torch.triu(
                torch.ones(
                    (seqlen, seqlen),
                    dtype=attention_scores.dtype,
                    device=attention_scores.device,
                )
                * float("-inf"),
                diagonal=1,
            )
        else:
            raise NotImplementedError()

        # attention scores and attention mask [b, np, sq, sk]
        attention_probs = F.softmax(attention_scores, dim=-1)

        # value_layer -> context layer.
        # [sk, b, np, hn] --> [b, np, sq, hn]

        # change view [sk, b * np, hn]
        value_layer = value_layer.reshape(
            value_layer.size(0), value_layer.size(1) * value_layer.size(2), -1
        )

        # change view [b * np, sq, sk]
        attention_probs = attention_probs.reshape(
            attention_probs.size(0) * attention_probs.size(1),
            attention_probs.size(2),
            -1,
        )

        # matmul: [b * np, sq, hn]
        context_layer = torch.bmm(attention_probs, value_layer.transpose(0, 1))

        # change view [b, np, sq, hn]
        context_layer = context_layer.reshape(
            batch_size, -1, context_layer.size(1), context_layer.size(2)
        )

        # [b, np, sq, hn] --> [sq, b, np, hn]
        context_layer = context_layer.permute(2, 0, 1, 3)

        # [sq, b, np, hn] --> [sq, b, hp]
        context_layer = context_layer.reshape(seqlen, batch_size, -1)

        return context_layer


class MultiHeadAttention(Module):
    """
    Replacement for te.attention.MultiHeadAttention
    """

    def __init__(
        self,
        hidden_size: int,
        num_attention_heads: int,
        kv_channels: int,
        layernorm_epsilon: float,
        attn_mask_type: str = "causal",
        params_dtype: torch.dtype = torch.float32,
        input_layernorm: bool = False,
        attention_type: str = "self",
        fuse_qkv_params: bool = False,
        zero_centered_gamma: bool = False,
        qkv_weight_interleaved: bool = True,
        bias: bool = True,
    ):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_attention_heads = num_attention_heads
        self.kv_channels = kv_channels
        self.layernorm_epsilon = layernorm_epsilon
        self.attn_mask_type = attn_mask_type
        self.params_dtype = params_dtype
        self.input_layernorm = input_layernorm
        self.attention_type = attention_type
        self.fuse_qkv_params = fuse_qkv_params
        self.zero_centered_gamma = zero_centered_gamma
        self.qkv_weight_interleaved = qkv_weight_interleaved and fuse_qkv_params
        self.bias = bias
        assert attn_mask_type == "causal"
        assert attention_type == "self"

        self.hidden_size_per_attention_head = kv_channels

        if self.input_layernorm:
            self.layernorm_qkv = LayerNormLinear(
                hidden_size,
                3 * hidden_size,
                eps=layernorm_epsilon,
                bias=bias,
                parameters_split=("query_", "key_", "value_")
                if not fuse_qkv_params
                else None,
                params_dtype=params_dtype,
            )
        else:
            self.qkv = Linear(
                hidden_size,
                3 * hidden_size,
                bias=bias,
                parameters_split=("query_", "key_", "value_")
                if not fuse_qkv_params
                else None,
                params_dtype=params_dtype,
            )

        self.core_attention = DotProductAttention(
            num_attention_heads, kv_channels, attn_mask_type=attn_mask_type
        )

        self.proj = Linear(hidden_size, hidden_size, bias=bias)

    def forward(
        self,
        hidden_states: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        rotary_pos_emb: Optional[
            Union[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]]
        ] = None,
        core_attention_bias_type: str = "no_bias",
    ) -> torch.Tensor:
        assert (
            attention_mask is None
            and rotary_pos_emb is None
            and core_attention_bias_type == "no_bias"
        )

        if self.input_layernorm:
            layernorm_qkv_outputs = self.layernorm_qkv.forward(hidden_states)
            mixed_x_layer = layernorm_qkv_outputs
        else:
            mixed_x_layer = self.qkv.forward(hidden_states)

        assert not mixed_x_layer.isnan().any()

        if self.qkv_weight_interleaved:
            # [sq, b, (np * 3 * hn)] --> [sq, b, np, 3 * hn]
            new_tensor_shape = mixed_x_layer.size()[:-1] + (
                self.num_attention_heads,
                3 * self.hidden_size_per_attention_head,
            )
            # split along last dimension
            split_dim = -1
        else:
            # [sq, b, (np * 3 * hn)] --> [sq, b, 3 * np, hn]
            new_tensor_shape = mixed_x_layer.size()[:-1] + (
                3 * self.num_attention_heads,
                self.hidden_size_per_attention_head,
            )
            # split along second last dimension
            split_dim = -2

        mixed_x_layer = mixed_x_layer.reshape(*new_tensor_shape)

        def split_tensor_along_dim(
            tensor: torch.Tensor, dim: int, num_partitions: int
        ) -> Tuple[torch.Tensor, ...]:
            """Split a tensor along its last dimension.
            Arguments:
                tensor: input tensor.
                num_partitions: number of partitions to split the tensor
                contiguous_split_chunks: If True, make each chunk contiguous
                                        in memory.
            """
            # Get the size and dimension.
            split_size = tensor.size()[dim] // num_partitions
            assert tensor.size()[dim] == split_size * num_partitions
            tensor_list = torch.split(tensor, split_size, dim=dim)
            # Note: torch.split does not create contiguous tensors by default.

            return tensor_list

        query_layer, key_layer, value_layer = split_tensor_along_dim(
            mixed_x_layer, split_dim, 3
        )
        assert rotary_pos_emb is None

        context_layer = self.core_attention.forward(
            query_layer, key_layer, value_layer, attention_mask
        )

        attention_output = self.proj.forward(context_layer)

        return attention_output


class TransformerLayer(Module):
    def __init__(
        self,
        hidden_size: int,
        ffn_hidden_size: int,
        num_attention_heads: int,
        layernorm_epsilon: float = 1e-5,
        kv_channels: Optional[int] = None,
        self_attn_mask_type: str = "causal",
        params_dtype: torch.dtype = torch.float32,
        seq_length: Optional[int] = None,
        micro_batch_size: Optional[int] = None,
        apply_residual_connection_post_layernorm: bool = False,
        output_layernorm: bool = False,
        fuse_qkv_params: bool = False,
        zero_centered_gamma: bool = False,
        qkv_weight_interleaved: bool = True,
        bias: bool = True,
        activation: str = "gelu",
    ):
        super().__init__()
        self.hidden_size = hidden_size
        self.ffn_hidden_size = ffn_hidden_size
        self.num_attention_heads = num_attention_heads
        self.layernorm_epsilon = layernorm_epsilon
        self.kv_channels = kv_channels or hidden_size // num_attention_heads
        self.self_attn_mask_type = self_attn_mask_type
        self.params_dtype = params_dtype
        self.seq_length = seq_length
        self.micro_batch_size = micro_batch_size
        self.apply_residual_connection_post_layernorm = (
            apply_residual_connection_post_layernorm
        )
        self.output_layernorm = output_layernorm
        self.fuse_qkv_params = fuse_qkv_params
        self.zero_centered_gamma = zero_centered_gamma
        self.qkv_weight_interleaved = qkv_weight_interleaved and fuse_qkv_params
        self.use_bias = bias
        self.activation = activation

        assert self_attn_mask_type == "causal"

        self.self_attention = MultiHeadAttention(
            hidden_size=hidden_size,
            num_attention_heads=num_attention_heads,
            kv_channels=self.kv_channels,
            layernorm_epsilon=layernorm_epsilon,
            attn_mask_type=self_attn_mask_type,
            params_dtype=params_dtype,
            input_layernorm=not output_layernorm,
            attention_type="self",
            fuse_qkv_params=fuse_qkv_params,
            zero_centered_gamma=zero_centered_gamma,
            qkv_weight_interleaved=qkv_weight_interleaved,
            bias=bias,
        )

        self.layernorm_mlp = LayerNormMLP(
            hidden_size=hidden_size,
            ffn_hidden_size=ffn_hidden_size,
            eps=layernorm_epsilon,
            bias=bias,
            activation=activation,
        )

        if output_layernorm:
            self.layernorm = LayerNorm(
                hidden_size, eps=layernorm_epsilon, dtype=params_dtype
            )

    def forward(
        self,
        hidden_states: torch.Tensor,
        # attention_mask: Optional[torch.Tensor] = None,
        # rotary_pos_emb: Optional[
        #     torch.Tensor | Tuple[torch.Tensor, torch.Tensor]
        # ] = None,
        # core_attention_bias_type: str = "no_bias",
        # core_attention_bias: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        attention_mask = None
        rotary_pos_emb = None
        core_attention_bias_type = "no_bias"
        core_attention_bias = None
        residual = hidden_states

        self_attention_outputs = self.self_attention.forward(
            hidden_states=hidden_states,
            attention_mask=attention_mask,
            rotary_pos_emb=rotary_pos_emb,
            core_attention_bias_type=core_attention_bias_type,
        )

        residual += self_attention_outputs
        mlp_outputs = self.layernorm_mlp.forward(residual)
        output = mlp_outputs + residual

        if self.output_layernorm:
            output = self.layernorm.forward(output)
        return output
