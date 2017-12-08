import unittest

from asm import evaluate_asm, perform_op, check_cond, evaluate_multiple_asm, \
        get_max_during_ops

class AsmTestCase(unittest.TestCase):
    def test_perform_op_default_value(self):
        self.assertEqual(perform_op('a', 'inc', 5, {}), {'a': 5})

    def test_perform_op_inc(self):
        self.assertEqual(perform_op('a', 'inc', 5, {'a': 3}), {'a': 8})
    
    def test_perform_op_dec(self):
        self.assertEqual(perform_op('a', 'dec', 5, {'a': 3}), {'a': -2})

    def check_cond_true(self):
        self.assertTrue(check_cond('a', '==', 0, {}))
        self.assertTrue(check_cond('a', '==', 3, {'a': 3}))
        self.assertFalse(check_cond('a', '==', 10, {'a': 3}))

    def test_variable_starts_at_zero(self):
        self.assertEqual(evaluate_asm('a inc 0 if a == 0', {}), {'a': 0})

    def test_increment(self):
        self.assertEqual(evaluate_asm('a inc 5 if a == 0', {}), {'a': 5})

    def test_false_cond_is_nop(self):
        self.assertEqual(evaluate_asm('a inc 5 if b == 10', {}), {})

    def test_evaluate_negative_inc(self):
        self.assertEqual(evaluate_asm('a inc -5 if a == 0', {}), {'a': -5})

    def test_evaluate_negative_cond(self):
        self.assertEqual(evaluate_asm('a inc -5 if a == -0', {}), {'a': -5})

    def test_evaluate_multiple_asm(self):
        ops = ['a inc 5 if a == 0']
        ops.append('b inc 10 if a == 5')
        ops.append('c inc 5 if a == 10')
        self.assertEqual(evaluate_multiple_asm(ops), {'a': 5, 'b': 10})

    def test_get_max_during_ops(self):
        ops = ['a inc 5 if a == 0']
        ops.append('b inc 10 if a == 5')
        ops.append('c inc 5 if a == 10')
        ops.append('b dec 15 if a == 5')
        self.assertEqual(get_max_during_ops(ops), 10)
