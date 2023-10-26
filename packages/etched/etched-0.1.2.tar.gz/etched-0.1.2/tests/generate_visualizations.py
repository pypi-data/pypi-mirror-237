import os

import pytest
import torch
import torch.nn as nn
import transformer_engine.pytorch as te

from etched.pytorch import compile

MODELS = [
    te.Linear(
        in_features=16,
        out_features=16,
    ),
    te.LayerNorm(
        hidden_size=16,
    ),
    te.LayerNormLinear(
        in_features=16,
        out_features=16,
    ),
    te.LayerNormMLP(
        hidden_size=16,
        ffn_hidden_size=16,
    ),
    te.TransformerLayer(
        hidden_size=16,
        num_attention_heads=2,
        ffn_hidden_size=16,
    ),
]


@pytest.mark.parametrize("model", MODELS)
def test_torch_fx_visualization(model: nn.Module):
    os.makedirs("visualizations", exist_ok=True)

    compiled_module: torch.fx.GraphModule = compile(
        model, example_input=torch.zeros((16, 16, 16), device="cuda")
    )
    print(
        f"{model.__class__.__name__} compiles to a graph with {len(compiled_module.graph.nodes)} nodes"
    )

    g = torch.fx.passes.graph_drawer.FxGraphDrawer(
        compiled_module, model.__class__.__name__
    )
    with open(f"visualizations/{model.__class__.__name__}.svg", "wb") as f:
        f.write(g.get_dot_graph().create_svg())
