#!/usr/bin/env python3
""""Module contains a unittest called TestAccessNestedMap"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
import utils


class TestAccessNestedMap(unittest.TestCase):
    """Unittests for methods given in the exercise"""

    @parameterized.expand([
        ({"a": 1}, ("a")),
        ({"a": {"b": 2}}, ("a")),
        ({"a": {"b": 2}}, ("a", "b"))
        ])
    def test_access_nested_map(self, nested_map, path):
        mapped = utils.access_nested_map(nested_map, path)
        self.assertEqual(mapped, nested_map[path[-1]])

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Class contains test cases for get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload):
        pass
