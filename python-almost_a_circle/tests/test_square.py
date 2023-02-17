#!/usr/bin/python3
"""Test class base"""

import unittest
from models.square import Square


class testbase(unittest.TestCase):
    """Class test Square"""

    """Tesst of Square"""
    """Test of Square with not integers"""

    def test_invalid_arg_type(self):
        """Invalid argument type on instantiation"""
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, "1", 2)
        self.assertRaises(TypeError, Square, "1", "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(TypeError, Square, 1, 2, 3, "4")


if __name__ == '__main__':
    unittest.main()
