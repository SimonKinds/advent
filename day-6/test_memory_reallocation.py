import unittest
from memory_reallocate import memory_reallocate

class MemoryReallocationTestCase(unittest.TestCase):
    def test_single_element_is_one(self):
       self.assertEqual(memory_reallocate([1])[0], 1) 
    
    def test_two_rounds(self):
        # [2, 0] => [1, 1]
        # [1, 1] => [0, 2]
        # [0, 2] => [1, 1]
        self.assertEqual(memory_reallocate([2, 0])[0], 3)

    def test_two_rounds(self):
        # [2, 0] => [1, 1]
        # [1, 1] => [0, 2]
        # [0, 2] => [1, 1]
        self.assertEqual(memory_reallocate([2, 0])[1], 2)