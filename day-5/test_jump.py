import unittest

from jump import jump, jump_part_two

class JumpTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(jump([0]), 2)
    
    def test_negative(self):
        self.assertEqual(jump([1, -1]), 3)
    
    def test_given(self):
        self.assertEqual(jump([0, 3, 0, 1, -3]), 5)

    def test_part_two(self):
        self.assertEqual(jump_part_two([0, 3, 0, 1, -3]), 10)
