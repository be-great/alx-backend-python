#!/usr/bin/env python3
"""
 Complex types - list of floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    function that sum the floating number
    """
    return float(sum(mxd_lst))
