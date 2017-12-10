import unittest

from knot_hash import knot_hash, dense_knot_hash, perform_xor, to_hex

class KnotHashTestCase(unittest.TestCase):
    def test_empty_length_list(self):
        self.assertEqual(knot_hash([]), 0)

    def test_zero_length(self):
        self.assertEqual(knot_hash([0]), 0)

    def test_length_reverses(self):
        self.assertEqual(knot_hash([3]), 2)

    def test_length_changes_pos(self):
        # 2, 1, [0]
        self.assertEqual(knot_hash([3, 2]), 2)
    
    def test_wraps_around(self):
        # 0, 1, 2, 3 | 3
        # 2, 1, 0, [3] | 2
        # 3, 1, 0, 2
        self.assertEqual(knot_hash([3, 2], max_value=3), 3)

    def test_skip_length_increases(self):
        # [0], 1, 2, 3 | 3
        # 2, 1, 0, [3] | 2 + 1
        # 3, 1, [0], 2 | 2 + 2
        # 3, 1, [2], 0 | 3 + 3
        self.assertEqual(knot_hash([3, 2, 2, 3], max_value=3), 2)

    def test_perform_xor(self):
        self.assertEqual(perform_xor(
            [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]), 64)

    def test_to_hex(self):
        self.assertEqual(to_hex([64, 7, 255]), '4007ff')

    def test_dense(self):
        self.assertEqual(dense_knot_hash(
            ''), 'a2582a3a0e66e6e86e3812dcb672a272')
        self.assertEqual(dense_knot_hash('AoC 2017'),
                         '33efeb34ea91902bb2f59c9920caa6cd')
        self.assertEqual(dense_knot_hash('1,2,3'),
                         '3efbe78a8d82f29979031a4aa0b16a9d')
        self.assertEqual(dense_knot_hash('1,2,4'),
                         '63960835bcdc130f0b66d7ff4f6a5a8e')
