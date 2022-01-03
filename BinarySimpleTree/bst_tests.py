import unittest
import random
from binary_simple_tree import BST, BSTFind, BSTNode


class TestBSTFind(unittest.TestCase):

    def test_tree_creation_and_find_method(self):
        test_tree = BST(None)
        test_tree.AddKeyValue(5, 'Friend')
        find_node = test_tree.FindNodeByKey(5)
        self.assertEqual(find_node.Node, test_tree.Root)

        test_left_find = test_tree.FindNodeByKey(2)
        self.assertEqual(test_left_find.ToLeft, True)
        self.assertEqual(test_left_find.NodeHasKey, False)
        self.assertEqual(test_left_find.Node, test_tree.Root)
        test_tree.AddKeyValue(2, 'Potato')
        self.assertEqual(test_tree.Root.LeftChild.NodeValue, 'Potato')

        test_left_find = test_tree.FindNodeByKey(6)
        self.assertEqual(test_left_find.ToLeft, False)
        self.assertEqual(test_left_find.NodeHasKey, False)
        self.assertEqual(test_left_find.Node, test_tree.Root)
        test_tree.AddKeyValue(6, 'Raspberry')
        self.assertEqual(test_tree.Root.RightChild.NodeValue, 'Raspberry')

        test_exist_key = test_tree.FindNodeByKey(6)
        self.assertEqual(test_exist_key.ToLeft, False)
        self.assertEqual(test_exist_key.NodeHasKey, True)
        self.assertEqual(test_exist_key.Node.NodeValue, 'Raspberry')

        # trying to add existing key
        test_tree.AddKeyValue(6, 'BoomBox')
        find_six_key = test_tree.FindNodeByKey(6)
        self.assertEqual(find_six_key.Node.NodeValue, 'Raspberry')

        # add some nodes
        test_tree.AddKeyValue(1, 'Im the One')
        test_tree.AddKeyValue(3, 'Thirsty Spartans')
        test_tree.AddKeyValue(4, 'Four')
        test_tree.AddKeyValue(7, 'Lucky')
        test_tree.AddKeyValue(8, 'Endless')
        test_tree.AddKeyValue(9, 'Not Six')

        max_from_root_test = test_tree.FinMinMax(test_tree.Root, True)
        min_from_root_test = test_tree.FinMinMax(test_tree.Root, False)
        self.assertEqual(max_from_root_test.NodeKey, 9)
        self.assertEqual(min_from_root_test.NodeKey, 1)

        define_subroot = test_tree.FindNodeByKey(6)
        subroot_node = define_subroot.Node
        max_from_subroot_test = test_tree.FinMinMax(subroot_node, True)
        min_from_subroot_test = test_tree.FinMinMax(subroot_node, False)

        self.assertEqual(max_from_subroot_test.NodeKey, 9)
        self.assertEqual(min_from_subroot_test.NodeKey, 6)

        #test Count
        self.assertEqual(test_tree.Count(), 9)

    def test_deletion(self):
        test_tree_2 = BST(None)

        test_tree_2.AddKeyValue(15, 'Root')
        test_tree_2.AddKeyValue(10, 'Branch')
        self.assertEqual(test_tree_2.Root.LeftChild.NodeValue, 'Branch')
        test_tree_2.DeleteNodeByKey(10)
        self.assertEqual(test_tree_2.Root.LeftChild, None)

        test_tree_2.AddKeyValue(10, 'Brahch')
        test_tree_2.AddKeyValue(8, 'SubBranch')
        test_tree_2.AddKeyValue(5, 'SubSubBranch')
        test_tree_2.AddKeyValue(4, 'Leaf1')
        test_tree_2.AddKeyValue(6, 'Leaf2')

        test_tree_2.DeleteNodeByKey(5)
        self.assertEqual(test_tree_2.FindNodeByKey(4).Node.Parent.NodeKey, 6)
        self.assertEqual(test_tree_2.FindNodeByKey(6).Node.LeftChild.NodeKey, 4)
        self.assertEqual(test_tree_2.FindNodeByKey(6).Node.RightChild, None)
        self.assertEqual(test_tree_2.FindNodeByKey(6).Node.Parent.NodeKey, 8)

        test_tree_2.AddKeyValue(12, 'Check')
        test_tree_2.AddKeyValue(14, 'DoubleCheck')

        test_tree_2.DeleteNodeByKey(10)

        self.assertEqual(test_tree_2.FindNodeByKey(12).Node.Parent, test_tree_2.Root)
        self.assertEqual(test_tree_2.Root.LeftChild.NodeKey, 12)
        self.assertEqual(test_tree_2.FindNodeByKey(12).Node.LeftChild.NodeKey, 8)

        # test Count
        self.assertEqual(test_tree_2.Count(), 6)


    def test_count(self):
        count_tree = BST(None)
        keys = random.sample(range(1, 9999), 1000)
        for i in keys:
            count_tree.AddKeyValue(i, str(random.randint(1000, 9999)))

        self.assertEqual(count_tree.Count(), 1000)

        empty_tree = BST(None)
        self.assertEqual(empty_tree.Count(), 0)