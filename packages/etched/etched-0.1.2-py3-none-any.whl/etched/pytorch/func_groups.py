"""
Sets and dictionaries of functions in torch_equivalent.py, iir.py, and sohu_ir.py with some property.
"""
import torch
from typing_extensions import Callable, Dict, Set

from .iir import *
from .torch_equivalent import *


def linear_funcs() -> Dict[Callable, Set[int]]:
    """
    Returns a dictionary whose keys are functions that are linear some of their arguments, and whose values are the indices of the arguments that are linear.
    """
    return {
        bmm: {0, 1},
        get_q: {0},
        get_k: {0},
        get_v: {0},
        transpose: {0},
        view: {0},
    }


def get_no_ops() -> Dict[Callable, int]:
    """
    Returns a dictionary whose keys are functions that simply return one of their arguments, and whose values are the indices of the arguments that they return.
    """
    return {dropout: 0, identity: 0, numToTensor: 0, tensorToInt: 0}


def get_activation_functions() -> Set[Callable[..., torch.Tensor]]:
    """
    Returns a set of activation functions that Sohu supports.
    """
    return {relu, gelu, silu}


def commutative_funcs() -> Set[Callable]:
    """
    Returns a set of functions that are commutative in their non-keyword arguments. Does not include functions with zero or one non-keyword arguments.
    """
    return {mul}


def batchprompt_size_preserving() -> Dict[Callable, Set[int]]:
    """
    Returns a dictionary whose keys are functions that preserve the batch and prompt dimension of one of their inputs, and the values are the indices of the argument that they preserve.
    """
    return {
        get_q: {0},
        get_k: {0},
        get_v: {0},
        layer_norm: {0},
        mul: {0, 1},
    }
