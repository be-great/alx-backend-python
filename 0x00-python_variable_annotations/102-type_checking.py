#!/usr/bin/env python3
"""
 11. More involved type annotations
"""
from typing import TypeVar, Any, Union, Tuple, List


T = TypeVar('T')


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Type Checking"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
