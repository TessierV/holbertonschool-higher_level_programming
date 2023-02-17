#!/usr/bin/python3
"""Test class base"""

import unittest
from models.rectangle import Rectangle


class testbase(unittest.TestCase):
    """Class test rectangle"""

    """Tesst of Rectangle"""
    """Test of Rectangle() for assigning automatically an ID exists"""

    def test_none(self):
        base = Rectangle()
        self.assertEqual(base.to_json_string([]), '[]')


if __name__ == '__main__':
    unittest.main()
