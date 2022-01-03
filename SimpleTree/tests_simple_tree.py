import unittest
from simple_tree import SimpleTree, SimpleTreeNode


class TestSimpleTree(unittest.TestCase):

    def test_basic_methods_working(self):
        # Create Tree and attach some 1lvl nodes
        root_node = SimpleTreeNode("ROOT", None)
        root_child_1 = SimpleTreeNode("Root boy", None)
        root_child_2 = SimpleTreeNode("Root boy 2", None)
        root_child_3 = SimpleTreeNode("Root boy 3", None)
        tree = SimpleTree(root_node)
        tree.AddChild(root_node, root_child_1)
        tree.AddChild(root_node, root_child_2)
        tree.AddChild(root_node, root_child_3)

        # check children linking
        self.assertEqual(root_node.Children, [root_child_1, root_child_2, root_child_3])
        for i in root_node.Children:
            self.assertEqual(i.Parent, root_node)

        # Create and attach few 2nd lvl children
        grandson_1 = SimpleTreeNode("grandson boy", None)
        grandson_2 = SimpleTreeNode("grandson boy 2", None)
        granddaughter = SimpleTreeNode("granddaughter", None)

        tree.AddChild(root_child_1, grandson_1)
        tree.AddChild(root_child_2, grandson_2)
        tree.AddChild(root_child_3, granddaughter)

        # checking GetAllNodes method
        self.assertEqual(len(tree.GetAllNodes()), 7)
        self.assertEqual(tree.GetAllNodes()[0], root_node)
        self.assertEqual(tree.GetAllNodes()[-1], granddaughter)

        # checking node with subtree deletion
        tree.DeleteNode(root_child_3)
        self.assertEqual(root_child_3 in tree.GetAllNodes(), False)
        self.assertEqual(granddaughter in tree.GetAllNodes(), False)

    def test_find_move_and_counts(self):
        # create testing tree and test find nodes method
        root_node = SimpleTreeNode("apple", None)
        root_child_1 = SimpleTreeNode("empty", None)
        root_child_2 = SimpleTreeNode("empty", None)
        root_child_3 = SimpleTreeNode("apple", None)
        tree = SimpleTree(root_node)
        tree.AddChild(root_node, root_child_1)
        tree.AddChild(root_node, root_child_2)
        tree.AddChild(root_node, root_child_3)

        grandchild_1 = SimpleTreeNode("apple", None)
        grandchild_2 = SimpleTreeNode("empty", None)
        grandchild_3 = SimpleTreeNode("empty", None)

        tree.AddChild(root_child_1, grandchild_1)
        tree.AddChild(root_child_2, grandchild_2)
        tree.AddChild(root_child_3, grandchild_3)

        appleleaf = SimpleTreeNode("apple", None)

        tree.AddChild(root_child_2, appleleaf)

        tryfind = tree.FindNodesByValue("apple")
        applelist = [tree.Root, grandchild_1, appleleaf, root_child_3]
        self.assertEqual(applelist, tryfind)

        # test node move method

        tree.MoveNode(root_child_3, appleleaf)
        self.assertEqual(root_child_3 in tree.Root.Children, False)
        self.assertEqual(root_child_3 in appleleaf.Children, True)
        self.assertEqual(grandchild_3 in root_child_3.Children, True)

        # test count

        self.assertEqual(tree.Count(), 8)
        self.assertEqual(tree.LeafCount(), 3)

        # allnodes = tree.GetAllNodes()
        # for i in allnodes:
        #     print(i.NodeValue)

    def test_nodelevels_marking(self):
        root_node = SimpleTreeNode("root", None)
        root_child_1 = SimpleTreeNode("1_st_level_node", None)
        root_child_2 = SimpleTreeNode("1_st_level_node", None)
        root_child_3 = SimpleTreeNode("1_st_initially_then_move_test", None)
        tree = SimpleTree(root_node)
        tree.AddChild(root_node, root_child_1)
        tree.AddChild(root_node, root_child_2)
        tree.AddChild(root_node, root_child_3)

        grandchild_1 = SimpleTreeNode("2nd_level_node", None)
        grandchild_2 = SimpleTreeNode("2nd_level_node", None)
        grandchild_3 = SimpleTreeNode("2nd_level_node", None)

        tree.AddChild(root_child_1, grandchild_1)
        tree.AddChild(root_child_2, grandchild_2)
        tree.AddChild(root_child_3, grandchild_3)

        # tree.MarkNodeTreeLevel()


        self.assertEqual(tree.Root.TreeLevel, 0)
        self.assertEqual(root_child_1.TreeLevel, 1)
        self.assertEqual(grandchild_1.TreeLevel, 2)

        tree.MoveNode(root_child_3, grandchild_1)
        self.assertEqual(root_child_3.TreeLevel, 3)
        self.assertEqual(grandchild_3.TreeLevel, 4)

        # allnodes = tree.GetAllNodes()
        # for i in allnodes:
        #     print(i.NodeValue, i.TreeLevel)