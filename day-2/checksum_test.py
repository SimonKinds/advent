import unittest

from checksum import checksum, checksum_divisable

class ChecksumTestCase(unittest.TestCase):
    def test_value_of_one_row(self):
        self.assertEqual(checksum([[1, 5, 2, 10]]), 9)

    def test_value_negative_number(self):
        self.assertEqual(checksum([[1, -5, 2, 10]]), 15)

    def test_multiple_rows(self):
        self.assertEqual(checksum([[1, 5, 2, 10], [6, 2, 3, 9]]), 16)

class ChecksumDivisableTestCase(unittest.TestCase):
    def test_value_of_one_row(self):
        self.assertEqual(checksum_divisable([[3, 5, 2, 10]]), 5)

    def test_value_negative_number(self):
        self.assertEqual(checksum_divisable([[3, -2, 5, 10]]), 2)

    def test_uses_max(self):
        self.assertEqual(checksum_divisable([[6, 5, 3, 9]]), 3)

    def test_multiple_rows(self):
        self.assertEqual(checksum_divisable([[3, 5, 2, 10], [6, 2, 3, 9]]), 5+3)