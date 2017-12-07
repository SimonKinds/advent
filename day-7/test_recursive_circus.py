import unittest

from recursive_circus import find_root_name, Disk, parse_disk, correct_weight_recursive

class RecursiveCircusTestCase(unittest.TestCase):
    def test_find_root_empty(self):
        self.assertEqual(find_root_name([]), None)
    
    def test_find_root_single(self):
        self.assertEqual(find_root_name([Disk(name='root', children=[])]), 'root')

    def test_find_root_one_layer(self):
        self.assertEqual(find_root_name([Disk(name='root', children=['leaf']),
                                    Disk(name='leaf', weight=1)]), 'root')
    def test_find_root_one_layer_unordered(self):
        self.assertEqual(find_root_name([
            Disk(name='leaf', weight=1), Disk(name='root', children=['leaf'])]), 'root')

    def test_parse_disk_without_children(self):
        self.assertEqual(parse_disk('abc (1337)'), Disk(name='abc', weight=1337))

    def test_parse_disk_with_single_child(self):
        self.assertEqual(parse_disk('abc (1337) -> def'), Disk(name='abc', weight=1337, children=['def']))

    def test_get_correct_weight_recursive_base(self):
        root = Disk(name='root', weight=5, children=[])

        self.assertEqual(correct_weight_recursive(root, [root]), (5, None))

    def test_get_correct_weight_recursive(self):
        root = Disk(name='root', weight=5, children=['leaf1', 'leaf2'])
        leaf1 = Disk('leaf1', weight=3)
        leaf2 = Disk('leaf2', weight=3)

        self.assertEqual(correct_weight_recursive(root, [root, leaf1, leaf2]), (11, None))

    def test_get_correct_weight_recursive_invalid_weight(self):
        root = Disk(name='root', weight=5, children=['node1'])
        node1 = Disk('node1', weight=1, children=['leaf1', 'leaf2', 'leaf3'])
        leaf1 = Disk('leaf1', weight=3)
        leaf2 = Disk('leaf2', weight=5)
        leaf3 = Disk('leaf3', weight=3)

        self.assertEqual(correct_weight_recursive(root, [root, leaf1, leaf2, leaf3, node1]), (15, 3))