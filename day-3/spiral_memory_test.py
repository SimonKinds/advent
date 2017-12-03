import unittest

from spiral_memory import spiral_memory_distance, spiral_memory_sum

class SpiralMemoryTestCase(unittest.TestCase):
    def test_one_is_zero(self):
        self.assertEqual(spiral_memory_distance(1), 0)

    def test_two_is_one(self):
        self.assertEqual(spiral_memory_distance(2), 1)

    def test_three_is_two(self):
        self.assertEqual(spiral_memory_distance(3), 2)

    def test_given(self):
        self.assertEqual(spiral_memory_distance(12), 3)
        self.assertEqual(spiral_memory_distance(23), 2)
        self.assertEqual(spiral_memory_distance(1024), 31)
    
    def test_given_sum(self):
        self.assertEqual(spiral_memory_sum(2), 4)
        self.assertEqual(spiral_memory_sum(4), 5)

if __name__ == '__main__':
    unittest.main()