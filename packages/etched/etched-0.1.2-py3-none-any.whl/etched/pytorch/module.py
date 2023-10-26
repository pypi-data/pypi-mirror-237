import torch.fx as fx
import torch.nn as nn
from typing_extensions import Callable, Iterator, Set

from .func_groups import batchprompt_size_preserving


class SohuGraph(fx.Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_aligned_nodes()

    def _set_aligned_nodes(self):
        self.aligned_nodes: Set[fx.Node] = set()
        for node in self.nodes:
            assert isinstance(node, fx.Node)
            if node.op == "placeholder":
                self.aligned_nodes.add(node)
            elif (
                isinstance(node.target, Callable)
                and (indices := batchprompt_size_preserving().get(node.target))
                is not None
            ):
                for i in indices:
                    if node.args[i] in self.aligned_nodes:
                        self.aligned_nodes.add(node)
                        break

    def create_node(self, *args, **kwargs):
        node = super().create_node(*args, **kwargs)
        if node.op == "placeholder":
            self.aligned_nodes.add(node)
        elif (
            isinstance(node.target, Callable)
            and (indices := batchprompt_size_preserving().get(node.target)) is not None
        ):
            for i in indices:
                if node.args[i] in self.aligned_nodes:
                    self.aligned_nodes.add(node)
                    break
        return node


class SohuModule(fx.GraphModule):
    def __init__(self, root: nn.Module, graph: SohuGraph, *args, **kwargs):
        super().__init__(root, graph, *args, **kwargs)
        graph._set_aligned_nodes()

    def nodes(self, reverse: bool = False) -> Iterator[fx.Node]:
        """
        Default fx.Graph.nodes does not type-check as returning fx.Node, so this method provides a type-hinted wrapper.
        """
        for node in (
            self.graph.nodes if not reverse else self.graph.nodes.__reversed__()
        ):
            assert isinstance(node, fx.Node)
            yield node
