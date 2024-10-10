#!/usr/bin/env python3
"""
 6. Complex types - list of floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function that sum the floating number
    """
    return float(sum(mxd_lst))
