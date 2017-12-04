import unittest

from passphrase import is_passphrase_valid, is_passphrase_valid_anagram

class PassphraseTestCase(unittest.TestCase):
    def test_single_ok(self):
        self.assertTrue(is_passphrase_valid('a'))

    def test_repeating_false(self):
        self.assertFalse(is_passphrase_valid('a a'))

    def test_anagram(self):
        self.assertTrue(is_passphrase_valid_anagram('abcde fghij'))
        self.assertFalse(is_passphrase_valid_anagram('abcde xyz ecdab'))