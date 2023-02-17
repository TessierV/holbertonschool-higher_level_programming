#!/usr/bin/python3
"""Test class base"""

import unittest
from models.square import Square


class testbase(unittest.TestCase):
    """Class test Square"""
    def test_invalid_arg_type(self):
        self.assertRaises(ValueError, Square, -1, 2)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 0, 2)
        self.assertRaises(ValueError, Square, 1, 0)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        self.assertRaises(ValueError, Square, 1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()
