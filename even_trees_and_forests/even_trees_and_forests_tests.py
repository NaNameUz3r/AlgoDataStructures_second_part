import unittest
from even_trees_and_forests import SimpleTreeNode, SimpleTree


class TestEvenTrees(unittest.TestCase):
    def test_three_branches(self):

        self.root_node = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.root_node)

        child_1 = SimpleTreeNode(2, self.root_node)
        self.tree.AddChild(self.root_node, child_1)
        child_2 = SimpleTreeNode(3, self.root_node)
        self.tree.AddChild(self.root_node, child_2)
        child_3 = SimpleTreeNode(4, self.root_node)
        self.tree.AddChild(self.root_node, child_3)

        self.assertEqual(self.tree.EvenTrees(), [])

        sub_child_1 = SimpleTreeNode(5, child_2)
        self.tree.AddChild(child_2, sub_child_1)

        self.assertEqual(self.tree.EvenTrees(), [self.root_node, child_2])