import unittest
from parameterized import parameterized
"""
0. Parameterize a unit test
"""


def TestAccessNestedMap(unittest.TestCase):
    """
    implement the test case for nested map,...
    """
    @parameterized.expand([
        ({"a": 1}, path=("a",)),
        ({"a": {"b": 2}}, path=("a",)),
        ({"a": {"b": 2}}, path=("a", "b"))
    ])
    def access_nested_map(self, map, path):
        level = map
        for key in path:
            if key in level:
                level = level[key]
            else:
                raise keyError(f"key {key} not found in the map")
        return level