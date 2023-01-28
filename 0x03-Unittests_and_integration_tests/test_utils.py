#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for Access Nested Map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nmap, npath, nresult):
        """method to test the return value of the function"""
        self.assertEqual(access_nested_map(nmap, npath), nresult)


if __name__ == "__main__":
    unittest.main()
