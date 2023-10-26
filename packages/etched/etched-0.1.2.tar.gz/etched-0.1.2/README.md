# Etched Integrations for SOHU ASIC

Etched provides 

## Installation

Software support for Etched chips can be installed via `pip`:

```bash
# Doesn't currently work, as this library hasn't been published
pip install etched
```
Note that by default, `TransformerEngine` and the relevant Hugging Face libraries are not installed. However, `TransformerEngine` is recommended for training models on GPUs before deploying them on Etched hardware. To install this, go to https://github.com/NVIDIA/TransformerEngine for installation instructions.

# Getting started

Etched's SOHU chip is an ASIC specialized for inference on Transformer models. It is not able to run arbitrary PyTorch code. However, Transformers trained and run on NVIDIA GPUs (or other models built with TransformerEngine) can be deployed on SOHU without modifications. To start, let's take the Pytorch example from [TransformerEngine's README](https://github.com/NVIDIA/TransformerEngine):

```python
import torch
import transformer_engine.pytorch as te
from transformer_engine.common import recipe

# Set dimensions.
in_features = 768
out_features = 3072
hidden_size = 2048

# Initialize model and inputs.
model = te.Linear(in_features, out_features, bias=True)
inp = torch.randn(hidden_size, in_features, device="cuda")

# Create an FP8 recipe. Note: All input args are optional.
fp8_recipe = recipe.DelayedScaling(margin=0, interval=1, fp8_format=recipe.Format.E4M3)

# Enable autocasting for the forward pass
with te.fp8_autocast(enabled=True, fp8_recipe=fp8_recipe):
    out = model(inp)

loss = out.sum()
loss.backward()
```

This will train a simple linear LLM using the FP8 data type. We can run this model on a GPU system by using:

```python
inp = torch.randn(hidden_size, in_features)
with torch.cuda.amp.autocast():
    out = model(inp)
```

Any model trained with Transformer Engine can be run on SOHU. To run instead on a SOHU chip:

```python
import etched.pytorch
inp = torch.randn(hidden_size, in_features)
compiled_model = etched.pytorch.compile(
    model,
    example_input=inp,
)
out = compiled_model(inp)
```

# Supported backends

Etched's SOHU chip has not yet been fabricated. To allow us to test our software stack beforehand, this compiler may be used with one of a few backends:
- **Verilated-Model Runtime**: To test the correctness of our Verilog code, models can be run on our Verilator chip simulation. Because the Verilator C Runtime is very efficient and parallelizes well, large LLMs can be run. However, it still takes minutes to get each token from a production-size LLM.
- **NVIDIA GPUs**: To test the production performance of Etched's complier stack, models can also be run _through_ our compiler with GPUs as a backend.
- **Physical Chips**: For FPGA + actual silicon - coming soon!

By default, NVIDIA GPUs are used as a backend. However, we can change this by specifying a backend when calling our compiled model:

```python
out = compiled_model(inp, backend="verilator")
```

All interfaces are subject to modification as chip development continues.

# Project management

GitHub issues will be used to keep track of development milestones.
