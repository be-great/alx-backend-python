#!/usr/bin/env python3
"""
 Complex types - list of floats
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, int | float]:
    """
    function returns a tuple
    """
    return (k, v**2)
