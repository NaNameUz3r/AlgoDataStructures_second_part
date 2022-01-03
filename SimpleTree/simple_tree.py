class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        if self.Parent is None:
            self.TreeLevel = 0
        else:
            self.TreeLevel = self.Parent.TreeLevel + 1


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        NewChild.TreeLevel = NewChild.Parent.TreeLevel + 1

    def DeleteNode(self, NodeToDelete):
        parent_node = NodeToDelete.Parent
        parent_node.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        nodes_summary_list = [self.Root]

        def get_child_nodes(node):
            for child in node.Children:
                nodes_summary_list.append(child)
                get_child_nodes(child)

        get_child_nodes(self.Root)
        return nodes_summary_list

    def FindNodesByValue(self, val):
        found_nodes = []

        if self.Root.NodeValue == val:
            found_nodes.append(self.Root)

        def find_valuable_nodes(node):
            for child in node.Children:
                if child.NodeValue == val:
                    found_nodes.append(child)
                find_valuable_nodes(child)

        find_valuable_nodes(self.Root)
        return found_nodes

    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent
        self.MarkNodeTreeLevel(OriginalNode.Parent)


    def Count(self):
        node_counter = 0
        if self.Root is not None:
            node_counter = len(self.GetAllNodes())

        return node_counter

    def LeafCount(self):
        leaf_counter = 0
        all_nodes = self.GetAllNodes()
        for node in all_nodes:
            if not node.Children:
                leaf_counter += 1
        return leaf_counter

    def MarkNodeTreeLevel(self, starting_node):

        def mark_nodes(node):
            for node in node.Children:
                node.TreeLevel = node.Parent.TreeLevel + 1
                mark_nodes(node)

        mark_nodes(starting_node)
