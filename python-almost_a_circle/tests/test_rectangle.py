#!/usr/bin/python3
"""Test class base"""

import unittest
from models.rectangle import Rectangle


class testbase(unittest.TestCase):
    """Class test rectangle"""

    """Tesst of Rectangle"""
    """Test of Rectangle() for assigning automatically an ID exists"""

    def test_empty(self):
        """ test with no arg """
        with self.assertRaises(TypeError):
            Rectangle()


if __name__ == '__main__':
    unittest.main()
