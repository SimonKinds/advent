import unittest

from stream_processing import score_stream, count_garbage

class StreamProcessingTestCase(unittest.TestCase):
    def test_score_stream_empty_group(self):
        self.assertEqual(score_stream('{}'), 1)
    def test_score_stream_nested_groups(self):
        self.assertEqual(score_stream('{{}}'), 3)

    def test_score_high_to_low(self):
        # 1 + 2 + 3 + 2
        self.assertEqual(score_stream('{{{}}{}}'), 8)

    def test_garbage_simple(self):
        self.assertEqual(score_stream('{<jhalksjhdka>}'), 1)

    def test_garbage_open_group_is_ignored(self):
        self.assertEqual(score_stream('{<{}>}'), 1)

    def test_garbage_open_group_is_ignored(self):
        self.assertEqual(score_stream('{<{}>}'), 1)

    def test_garbage_exclamation_ignores_next(self):
        self.assertEqual(score_stream('{<!>{}>{}}'), 3)

    def test_garbage_exclamation_ignores_next(self):
        self.assertEqual(score_stream('{<!!>{}{}}'), 5)

    def test_given(self):
        self.assertEqual(score_stream('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)

    def test_count_garbage_only_groups(self):
        self.assertEqual(count_garbage('{{}{}}'), 0)

    def test_count_garbage_empty_garbage(self):
        self.assertEqual(count_garbage('{<>}'), 0)

    def test_count_garbage_character_in_garbage(self):
        self.assertEqual(count_garbage('{<aa>}'), 2)

    def test_count_garbage_doesnt_count_ignored(self):
        self.assertEqual(count_garbage('{<!aa>}'), 1)
