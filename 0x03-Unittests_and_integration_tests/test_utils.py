#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json, memoize, access_nested_map
"""
0. Parameterize a unit test
"""


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
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ a Test to test raise a KeyError is raised for the inputs """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


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
            """the class for the memoize method"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method') as mock_method:
            instance = TestClass()
            res1 = instance.a_property()
            res2 = instance.a_property()
            self.assertEqual(res1, 42)  # Check first result
            self.assertEqual(res2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
