import unittest

from passphrase import is_passphrase_valid

class PassphraseTestCase(unittest.TestCase):
    def test_single_ok(self):
        self.assertTrue(is_passphrase_valid('a'))

    def test_repeating_false(self):
        self.assertFalse(is_passphrase_valid('a a'))