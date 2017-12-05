import unittest

from jump import jump

class JumpTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(jump([0]), 2)
    
    def test_negative(self):
        self.assertEqual(jump([1, -1]), 3)
    
    def test_given(self):
        self.assertEqual(jump([0, 3, 0, 1, -3]), 5)