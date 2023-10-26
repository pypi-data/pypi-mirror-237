import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import transformer_engine.pytorch as te
from torchvision import datasets, transforms

import etched.pytorch


class TransformerLike(nn.Module):
    """Transformer-like network designed for MNIST. This does substantially
    worse than MNIST"""

    def __init__(self, d_model):
        super(TransformerLike, self).__init__()
        self.ln_proj = te.Linear(784, d_model, bias=False)
        self.dropout = torch.nn.Dropout(0.1)
        self.ln_mlp = te.LayerNormMLP(d_model, d_model * 4)
        self.fc3 = te.LayerNormLinear(d_model, 10)

    def forward(self, x):
        x = self.ln_proj(x)
        x = self.dropout(x)
        x = self.ln_mlp(x)
        x = self.fc3(x)
        return x


def check_model(model, device, test_loader, use_fp8):
    """Testing function."""
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            with te.fp8_autocast(enabled=use_fp8):
                output = model(data)
            test_loss += F.nll_loss(
                output, target, reduction="sum"
            ).item()  # sum up batch loss
            pred = output.argmax(
                dim=1, keepdim=True
            )  # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)

    print(
        f"\nTest set: Average loss: {test_loss:.4f}, "
        f"Accuracy: {correct}/{len(test_loader.dataset)} "
        f"({100. * correct / len(test_loader.dataset):.0f}%)\n"
    )


def test_training_inference_workflow():
    # Load the MNIST dataset from Pytorch's data loader
    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,)),
            torch.flatten,
        ]
    )
    dataset1 = datasets.MNIST("../data", train=True, download=True, transform=transform)
    dataset2 = datasets.MNIST("../data", train=False, transform=transform)
    train_loader = torch.utils.data.DataLoader(dataset1, batch_size=64)
    test_loader = torch.utils.data.DataLoader(dataset2, batch_size=64)

    # Instantiate our model and an Adam optimizer
    model = TransformerLike(256).cuda()
    optimizer = optim.Adam(model.parameters())

    # Should take ~5 seconds per epoch on an NVIDIA 4090 GPU
    # We should get >95% top-1 accuracy after 1 epoch
    for epoch in range(1):
        model.train()
        for data, labels in train_loader:
            data, labels = data.cuda(), labels.cuda()
            optimizer.zero_grad()
            with te.fp8_autocast(enabled=False):
                output = F.log_softmax(model(data), dim=1)
            loss = F.nll_loss(output, labels)
            loss.backward()
            optimizer.step()
    # Load a single test batch
    model.eval()
    data, labels = next(iter(test_loader))

    # Run the single test batch on our GPU
    with te.fp8_autocast(enabled=False):
        gpu_output = F.log_softmax(model(data.cuda()), dim=1).cpu()
    gpu_predicted = gpu_output.argmax(dim=1)
    gpu_num_correct = gpu_predicted.eq(labels).sum().item()
    assert gpu_num_correct >= 56  # We should get at least ~60/64 right
    print(f"GPU accuracy: {gpu_num_correct}/64 ({100. * gpu_num_correct / 64:.0f}%)")

    # Now do the same exact thing with SOHU's simulation
    compiled_module = etched.pytorch.compile(
        model,
        example_input=data.cuda(),
        verbosity=1,
    ).cuda()
    print(compiled_module)
    for node in compiled_module.graph.nodes:
        if node.op != "get_attr":
            print(node)
    sohu_predicted = (
        F.log_softmax(compiled_module(data.cuda()), dim=1).cpu().argmax(dim=1)
    )
    sohu_num_correct = sohu_predicted.eq(labels).sum().item()
    assert sohu_num_correct == gpu_num_correct
