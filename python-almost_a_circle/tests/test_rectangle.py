#!/usr/bin/python3
"""Test class base"""

import unittest
from models.rectangle import Rectangle


class testbase(unittest.TestCase):
    """Class test rectangle"""

    """Tesst of Rectangle"""
    """Test of Rectangle() for assigning automatically an ID exists"""
    def test_save1(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), '[]')


if __name__ == '__main__':
    unittest.main()
