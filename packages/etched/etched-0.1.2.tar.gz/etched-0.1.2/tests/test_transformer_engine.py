import os

import torch
import torch.nn as nn
import transformer_engine.pytorch as te
from hypothesis import Verbosity, assume, given, settings
from hypothesis import strategies as st
from typing_extensions import Callable, List, Optional, Tuple

from etched.pytorch import compile
from etched.pytorch.utils import never

_SKIP_ASSERTIONS = os.environ.get("SKIP_ASSERTIONS", "0") == "1"

default_init_method = te.utils.get_default_init_method()  # type: ignore

settings.register_profile(
    "transformer_engine",
    settings(
        deadline=None,
        verbosity=Verbosity.verbose,
        report_multiple_bugs=False,
        # max_examples=1,
    ),
)
settings.load_profile("transformer_engine")

torch.manual_seed(42)

GLOBAL_COUNTER = 0
SUCCESSES = set()


@given(
    in_features=st.integers(min_value=1, max_value=12288 // 16),
    out_features=st.integers(min_value=1, max_value=12288 // 16),
    bias=st.booleans(),
    params_dtype=st.sampled_from([torch.float32, torch.float16, torch.bfloat16]),
    parameters_split=st.one_of(
        st.none(),
        st.lists(
            st.text(alphabet="abcdefghijklmnopqrstuvwxyz"), min_size=1, unique=True
        ),
    ),
    bsz=st.integers(min_value=1, max_value=256 // 16),
)
def test_te_linear(
    in_features: int,
    out_features: int,
    bias: bool,
    params_dtype: torch.dtype,
    parameters_split: Optional[Tuple[str, ...]],
    bsz: int,
):
    parameters_split = tuple(parameters_split) if parameters_split is not None else None
    split_len = len(parameters_split) if parameters_split is not None else 1
    in_features = 16 * in_features
    out_features = 16 * out_features * split_len
    bsz = 16 * bsz

    while True:
        torch.cuda.empty_cache()

        torch.manual_seed(42)
        try:
            module = te.Linear(
                in_features,
                out_features,
                bias=bias,
                params_dtype=params_dtype,
                parameters_split=parameters_split,
            )
            inp = torch.randn(bsz, in_features, dtype=params_dtype, device="cuda")
            out: torch.Tensor = module(inp)

            compiled_module = compile(
                module,
                example_input=torch.zeros_like(inp, device="cuda"),
                verbosity=1,
            ).cuda()
            compiled_out: torch.Tensor = compiled_module(inp)
            break
        except torch.cuda.OutOfMemoryError:
            if (
                test_te_linear,
                in_features,
                out_features,
                bias,
                params_dtype,
                parameters_split,
                bsz,
            ) in SUCCESSES:
                print(
                    f"Memory error in test_te_linear with in_feature={in_features}, out_features={out_features}, bias={bias}, params_dtype={params_dtype}, parameters_split={parameters_split}, bsz={bsz}, retrying..."
                )
                continue
            else:
                return
    global GLOBAL_COUNTER
    print(GLOBAL_COUNTER := GLOBAL_COUNTER + 1)
    max_abs_diff = (out - compiled_out).abs().max().item()
    mean_abs_diff = (out - compiled_out).abs().mean().item()
    max_tol, mean_tol = (
        (1e-2, 1e-3)
        if params_dtype == torch.float32
        else (2e-2, 1e-3)
        if params_dtype == torch.float16
        else (7e-2, 5e-3)
        if params_dtype == torch.bfloat16
        else never()
    )
    assert _SKIP_ASSERTIONS or (
        max_abs_diff < max_tol and mean_abs_diff < mean_tol
    ), print(
        f"te_linear test failed with max_abs_diff {max_abs_diff}/{max_tol}, mean_abs_diff {mean_abs_diff}/{mean_tol}"
    )
    print(
        f"te_linear test passed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )
    SUCCESSES.add(
        (
            test_te_linear,
            in_features,
            out_features,
            bias,
            params_dtype,
            parameters_split,
            bsz,
        )
    )


@given(
    hidden_size=st.integers(min_value=1, max_value=768),
    bsz=st.integers(min_value=1, max_value=256),
    eps=st.floats(min_value=1e-16, max_value=1e-0),
)
def test_te_norms(hidden_size: int, bsz: int, eps: float):
    hidden_size = 16 * hidden_size
    bsz = 16 * bsz
    torch.manual_seed(42)
    module = te.LayerNorm(hidden_size, eps=eps).cuda()
    inp = torch.randn(bsz, hidden_size).cuda()
    out: torch.Tensor = module(inp).cpu()

    compiled_module = compile(
        module,
        example_input=torch.zeros_like(inp, device="cuda"),
        verbosity=1,
    ).cuda()
    compiled_out: torch.Tensor = compiled_module(inp).cpu()
    global GLOBAL_COUNTER
    print(GLOBAL_COUNTER := GLOBAL_COUNTER + 1)
    max_abs_diff = (out - compiled_out).abs().max().item()
    mean_abs_diff = (out - compiled_out).abs().mean().item()
    assert _SKIP_ASSERTIONS or (max_abs_diff < 1e-4 and mean_abs_diff < 1e-4), print(
        f"test_te_norms failed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )
    print(
        f"test_te_norms passed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )


@given(
    in_features=st.integers(min_value=16 // 16, max_value=1024 // 16),
    out_features=st.integers(min_value=16 // 16, max_value=1024 // 16),
    bias=st.booleans(),
    eps=st.floats(min_value=1e-16, max_value=1e-3),
    parameters_split=st.one_of(
        st.none(),
        st.lists(
            st.text(alphabet="abcdefghijklmnopqrstuvwxyz"), min_size=1, unique=True
        ),
    ),
    params_dtype=st.sampled_from([torch.float32, torch.float16, torch.bfloat16]),
    bsz=st.integers(min_value=16 // 16, max_value=256 // 16),
)
def test_te_layernormlinear(
    in_features: int,
    out_features: int,
    bias: bool,
    eps: float,
    parameters_split: Optional[Tuple[str, ...]],
    params_dtype: torch.dtype,
    bsz: int,
):
    torch.cuda.empty_cache()
    in_features *= 16
    out_features *= 16 * (len(parameters_split) if parameters_split is not None else 1)
    bsz *= 16
    torch.manual_seed(42)
    module = te.LayerNormLinear(
        in_features,
        out_features,
        bias=bias,
        eps=eps,
        parameters_split=parameters_split,
        params_dtype=params_dtype,
    )
    inp = torch.randn(bsz, in_features, dtype=params_dtype, device="cuda")
    out: torch.Tensor = module(inp).cpu()

    compiled_module = compile(
        module,
        example_input=torch.zeros_like(inp, dtype=params_dtype, device="cuda"),
        verbosity=1,
    ).cuda()
    global GLOBAL_COUNTER
    print(GLOBAL_COUNTER := GLOBAL_COUNTER + 1)
    compiled_out: torch.Tensor = compiled_module(inp).cpu()

    max_abs_diff = (out - compiled_out).abs().max().item()
    mean_abs_diff = (out - compiled_out).abs().mean().item()
    assert _SKIP_ASSERTIONS or (max_abs_diff < 1e-1 and mean_abs_diff < 4e-3), print(
        f"test_te_layernormlinear failed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )
    print(
        f"test_te_layernormlinear passed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )


@given(
    hidden_size=st.integers(min_value=1, max_value=12288 // 16),
    ffn_hidden_size=st.integers(min_value=1, max_value=12288 // 16),
    bias=st.booleans(),
    eps=st.floats(min_value=1e-16, max_value=1e-3),
    activation=st.sampled_from(["relu", "gelu"]),
    bsz=st.integers(min_value=1, max_value=256 // 16),
)
def test_te_layernorm_mlp(
    hidden_size: int,
    ffn_hidden_size: int,
    eps: float,
    bias: bool,
    activation: str,
    bsz: int,
):
    torch.cuda.empty_cache()
    hidden_size *= 16
    ffn_hidden_size *= 16
    bsz *= 16
    torch.manual_seed(42)
    module = te.LayerNormMLP(
        hidden_size, ffn_hidden_size, eps=eps, bias=bias, activation=activation
    ).cuda()
    inp = torch.randn(bsz, hidden_size, device="cuda")
    out: torch.Tensor = module(inp).cpu()

    compiled_module = compile(
        module,
        example_input=torch.zeros_like(inp, device="cuda"),
        verbosity=1,
    ).cuda()
    global GLOBAL_COUNTER
    print(GLOBAL_COUNTER := GLOBAL_COUNTER + 1)
    compiled_out: torch.Tensor = compiled_module(inp).cpu()

    max_abs_diff = (out - compiled_out).abs().max().item()
    mean_abs_diff = (out - compiled_out).abs().mean().item()
    assert _SKIP_ASSERTIONS or (max_abs_diff < 1e-2 and mean_abs_diff < 1e-3), print(
        f"test_te_layernorm_mlp failed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )
    print(
        f"test_te_layernorm_mlp passed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )


@given(
    head_dim=st.integers(min_value=16 // 16, max_value=32 // 16),
    num_attention_heads=st.integers(min_value=16 // 16, max_value=32 // 16),
    ffn_hidden_size=st.integers(min_value=16 // 16, max_value=32 // 16),
    layernorm_epsilon=st.floats(min_value=1e-16, max_value=1e-3),
    apply_residual_connection_post_layernorm=st.sampled_from([False]),
    output_layernorm=st.sampled_from([False]),
    self_attn_mask_type=st.sampled_from(["causal"]),
    bias=st.booleans(),
    activation=st.sampled_from(["relu", "gelu"]),
    bsz=st.integers(min_value=16 // 16, max_value=32 // 16),
    seq_len=st.integers(min_value=16 // 16, max_value=32 // 16),
)
def test_te_transformerlayer(
    head_dim: int,
    num_attention_heads: int,
    ffn_hidden_size: int,
    layernorm_epsilon: float,
    apply_residual_connection_post_layernorm: bool,
    output_layernorm: bool,
    self_attn_mask_type: str,
    bias: bool,
    activation: str,
    bsz: int,
    seq_len: int,
):
    torch.cuda.empty_cache()
    head_dim *= 16
    num_attention_heads *= 16
    hidden_size = head_dim * num_attention_heads
    ffn_hidden_size *= 16
    bsz *= 16
    seq_len *= 16
    torch.manual_seed(42)
    global GLOBAL_COUNTER
    print(GLOBAL_COUNTER := GLOBAL_COUNTER + 1)
    try:
        module = te.TransformerLayer(
            hidden_size=hidden_size,
            ffn_hidden_size=ffn_hidden_size,
            num_attention_heads=num_attention_heads,
            layernorm_epsilon=layernorm_epsilon,
            apply_residual_connection_post_layernorm=apply_residual_connection_post_layernorm,
            output_layernorm=output_layernorm,
            self_attn_mask_type=self_attn_mask_type,
            bias=bias,
            activation=activation,
            hidden_dropout=0.0,
        )
        module.eval()
        inp = torch.randn(bsz, seq_len, hidden_size, device="cuda")
        output = module.forward(inp)

        compiled_module = compile(
            module,
            example_input=torch.zeros_like(inp, device="cuda"),
            verbosity=1,
        ).cuda()
        equiv_output: torch.Tensor = compiled_module(inp)
        max_abs_diff = (output - equiv_output).abs().max().item()
        mean_abs_diff = (output - equiv_output).abs().mean().item()
    except torch.cuda.OutOfMemoryError:
        assume(False)
        return
    except Exception as e:
        print(e)
        raise e
    assert _SKIP_ASSERTIONS or (max_abs_diff < 1e-2 and mean_abs_diff < 1e-3), print(
        f"test_te_transformerlayer failed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )
    print(
        f"test_te_transformerlayer passed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )


@given(
    module_constructor_list=st.lists(
        st.sampled_from(
            [
                lambda emd_dim: te.Linear(emd_dim, emd_dim),
                lambda emd_dim: te.LayerNorm(emd_dim),
                lambda emd_dim: te.LayerNormLinear(emd_dim, emd_dim),
                lambda emd_dim: te.LayerNormMLP(emd_dim, 4 * emd_dim),
                lambda emd_dim: nn.Linear(emd_dim, emd_dim),
                lambda emd_dim: nn.LayerNorm(emd_dim),
                lambda emd_dim: nn.ReLU(),
                lambda emd_dim: nn.GELU(),
                lambda emd_dim: nn.SiLU(),
            ]
        ),
        min_size=1,
    ),
    embed_dim=st.integers(min_value=1, max_value=768),
    bsz=st.integers(min_value=1, max_value=256),
)
def test_sequential(
    module_constructor_list: List[Callable[[int], nn.Module]],
    embed_dim: int,
    bsz: int,
):
    global GLOBAL_COUNTER
    print(GLOBAL_COUNTER := GLOBAL_COUNTER + 1)
    torch.cuda.empty_cache()
    embed_dim *= 16
    bsz *= 16
    torch.manual_seed(42)
    try:
        module_list = [
            module_constructor(embed_dim)
            for module_constructor in module_constructor_list
        ]
        seq_module = nn.Sequential(*module_list).cuda()
        inp = torch.randn(bsz, embed_dim)
        out: torch.Tensor = seq_module(inp.cuda()).cpu()

        compiled_module = compile(
            seq_module, example_input=torch.zeros_like(inp), verbosity=1
        ).cuda()
        compiled_out: torch.Tensor = compiled_module(inp.cuda()).cpu()

        max_abs_diff = (out - compiled_out).abs().max().item()
        mean_abs_diff = (out - compiled_out).abs().mean().item()
    except torch.cuda.OutOfMemoryError:
        assume(False)
        return
    except Exception as e:
        print(e)
        raise e
    assert _SKIP_ASSERTIONS or (max_abs_diff < 3e-2 and mean_abs_diff < 8e-3), print(
        f"test_sequential with {len(module_list)} modules failed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )
    print(
        f"test_sequential with {len(module_list)} modules passed with max_abs_diff {max_abs_diff}, mean_abs_diff {mean_abs_diff}"
    )
