#!/usr/bin/env python3
import unittest
from parameterized import parameterized

"""
0. Parameterize a unit test
"""


# Define the access_nested_map function
def access_nested_map(map, path):
    """the nested map logic"""
    level = map
    for key in path:
        if key in level and isinstance(level, dict):
            level = level[key]
        else:
            raise KeyError(f"Key {key} not found in the map")
    return level


class TestAccessNestedMap(unittest.TestCase):
    """
    Implement the test case for nested map.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        The test logic
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for missing keys."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
