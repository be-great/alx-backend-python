#!/usr/bin/env python3
"""
 9. Let's duck type an iterable object
"""
from typing import List, Union, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element length"""
    return [(i, len(i)) for i in lst]
