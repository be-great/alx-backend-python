#!/usr/bin/env python3
"""
 8.Complex types - list of floats
"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function returns a multipler
    """
    def fun(n: float) -> float:
        return n * multiplier

    return fun
