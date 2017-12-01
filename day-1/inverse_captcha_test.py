import unittest
from inverse_captcha import inverse_captcha, inverse_captcha_from_string


class InverseCaptchaTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(inverse_captcha([]), 0)

    def test_no_equal(self):
        self.assertEqual(inverse_captcha([1, 2]), 0)

    def test_simple(self):
        self.assertEqual(inverse_captcha([1, 1, 5]), 1)

    def test_wrapping(self):
        self.assertEqual(inverse_captcha([9, 1, 9]), 9)

    def test_given(self):
        self.assertEqual(inverse_captcha([1, 1, 2, 2]), 3)
        self.assertEqual(inverse_captcha([1, 1, 1, 1]), 4)
        self.assertEqual(inverse_captcha([1, 2, 3, 4]), 0)
        self.assertEqual(inverse_captcha([9, 1, 2, 1, 2, 1, 2, 9]), 9)

    def test_from_string(self):
        self.assertEqual(inverse_captcha_from_string('1111'), 4)
        self.assertEqual(inverse_captcha_from_string('1234'), 0)