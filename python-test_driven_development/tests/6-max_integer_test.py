#!/usr/bin/python3
"""test for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    
    def test_max_beguinnning(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)
    
    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)
    
    def test_one_negativ(self):
        self.assertEqual(max_integer([-1, 2, 3]), 3)
    
    def test_all_negativ(self):
        self.assertEqual(max_integer([-1, -2, -3]), -3)
    
    def test_one_negativ(self):
        self.assertEqual(max_integer([]), None)
