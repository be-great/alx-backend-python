#!/usr/bin/env python3
"""
 10. Duck typing - first element of a sequence
"""
from typing import List, Union, Tuple, Iterable, Sequence, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    list : Sequence
    """
    if lst:
        return lst[0]
    else:
        return None
