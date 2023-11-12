#!/usr/bin/env python3
""""""
from typing import Any, Mapping, Sequence
import unittest
from unittest.mock import patch
from parameterized import parameterized

access_nested_map = __import__("utils").access_nested_map
utils = __import__("utils")


class TestAccessNestedMap(unittest.TestCase):
    """"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected: Any):
        """"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Mapping):
        """"""
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(utils.get_json(url), payload)
            mock_get.assert_called_once_with(url)
