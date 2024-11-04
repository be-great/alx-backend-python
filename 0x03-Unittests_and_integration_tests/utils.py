#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    nasted access map
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """
    Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """
    Decorator to memoize a method.
    Example:-
    of what we have
    ---------------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 11
    >>> my_obj = MyClass()
    >>> my_obj.a_method
    a_method called
    11
    >>> my_obj.a_method
    11
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
