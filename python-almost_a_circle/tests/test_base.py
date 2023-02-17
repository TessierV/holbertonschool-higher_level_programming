#!/usr/bin/python3
"""Test class base"""
#!/usr/bin/python3
"""Test class base"""

import unittest
from models.base import Base


class testbase(unittest.TestCase):
    """Class test base"""

    """Test of Base() for assigning automatically an ID exists"""
    def test_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
    """Test of Base() for assigning automatically an ID + 1 of the previous exists"""
    def test_id_prev(self):
        base = Base()
        self.assertEqual(base.id, 2)
    """Test of Base(89) saving the ID passed exists"""
    def test_id_pass(self):
        base = Base(89)
        self.assertEqual(base.id, 89)
    """Test of Base.to_json_string(None) exists"""
    def test_none(self):
        base = Base()
        self.assertEqual(base.to_json_string([]), '[]')

if __name__ == '__main__':
    unittest.main()
