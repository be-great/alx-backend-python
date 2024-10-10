#!/usr/bin/env python3
"""
 11. More involved type annotations
"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


# The types of the elements of the input are not know
def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Add dictonry and Typ"""
    if key in dct:
        return dct[key]
    else:
        return default
