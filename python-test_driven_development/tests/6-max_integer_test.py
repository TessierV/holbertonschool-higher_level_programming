#!/usr/bin/python3
"""test for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_results(self):
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([3, 2, 1]), 3)
        self.assertAlmostEqual(max_integer([1, 3, 2]),3)

if __name__ == '__main__':
    unittest.main()
