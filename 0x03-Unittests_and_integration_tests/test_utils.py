#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json, memoize
"""
0. Parameterize a unit test
"""


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
        ({"a": 1}, ("a", "b")),
        ({}, ("a",)),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for missing keys."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests or the get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": True}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected payload."""
        with patch('requests.get') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = test_payload

            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""

    def test_memoize(self):
        """Test that a_method is only called once with memoize."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mock_method:
            instance = TestClass()
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
