class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None
        if self.Root is not None:
            self.NodeCounter = 1
        else:
            self.NodeCounter = 0

    def FindNodeByKey(self, key):

        def parse_tree(target_key, parent_node=None):
            if parent_node is None:
                parent_node = self.Root

            next_parent_node = None

            if parent_node.NodeKey == target_key:
                return {
                    'Node': parent_node,
                    'NodeHasKey': True,
                    'ToLeft': False
                }
            elif target_key >= parent_node.NodeKey:
                next_parent_node = parent_node.RightChild
            elif target_key < parent_node.NodeKey:
                next_parent_node = parent_node.LeftChild

            if next_parent_node is not None:
                return parse_tree(target_key, next_parent_node)

            return {
                'Node': parent_node,
                'NodeHasKey': False,
                'ToLeft': True if parent_node.NodeKey > target_key else False
            }

        try_find_node = parse_tree(key)
        found_node = BSTFind()
        found_node.Node = try_find_node['Node']
        found_node.NodeHasKey = try_find_node['NodeHasKey']
        found_node.ToLeft = try_find_node['ToLeft']

        return found_node

    def AddKeyValue(self, key, val):

        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            self.NodeCounter += 1
            return True

        try_find = self.FindNodeByKey(key)

        if try_find.NodeHasKey is True:
            return False

        if try_find.ToLeft is True:
            try_find.Node.LeftChild = BSTNode(key, val, try_find.Node)
        else:
            try_find.Node.RightChild = BSTNode(key, val, try_find.Node)

        self.NodeCounter += 1
        return True

    def FinMinMax(self, FromNode, FindMax):

        def parse_tree(parent_node=None, find_max=False):
            if parent_node is None:
                parent_node = self.Root

            if find_max and parent_node.RightChild is not None:
                return parse_tree(parent_node.RightChild, find_max)
            elif find_max is False and parent_node.LeftChild is not None:
                return parse_tree(parent_node.LeftChild, find_max)

            return parent_node

        return parse_tree(FromNode, FindMax)

    def DeleteNodeByKey(self, key):
        kill_node = self.FindNodeByKey(key)
        if kill_node.NodeHasKey is False:
            return False

        if kill_node.Node.LeftChild is None and (
                kill_node.Node.RightChild is None):
            if kill_node.Node is self.Root:
                self.Root = None
                self.NodeCounter -= 1
                return True
            if kill_node.Node.NodeKey < kill_node.Node.Parent.NodeKey:
                kill_node.Node.Parent.LeftChild = None
            else:
                kill_node.Node.Parent.RightChild = None
            self.NodeCounter -=1
            return True

        if kill_node.Node.LeftChild is None or (
                kill_node.Node.RightChild is None):
            if kill_node.Node.LeftChild is None:
                orphan_need_parent = kill_node.Node.RightChild
            else:
                orphan_need_parent = kill_node.Node.LeftChild

            if kill_node.Node is self.Root:
                self.Root = orphan_need_parent
                self.Root.Parent = None
                self.NodeCounter -= 1
                return True

            if kill_node.Node.NodeKey < kill_node.Node.Parent.NodeKey:
                kill_node.Node.Parent.LeftChild = orphan_need_parent
            else:
                kill_node.Node.Parent.RightChild = orphan_need_parent

            orphan_need_parent.Parent = kill_node.Node.Parent
            self.NodeCounter -= 1
            return True

        if kill_node.Node.LeftChild is not None and (
                kill_node.Node.RightChild is not None):
            scoped_node = kill_node.Node.RightChild
            while scoped_node.LeftChild is not None:
                scoped_node = scoped_node.LeftChild
            if scoped_node.RightChild is None:
                scoped_node.LeftChild = kill_node.Node.LeftChild
                scoped_node.LeftChild.Parent = scoped_node
                if kill_node.Node.RightChild is not scoped_node:
                    scoped_node.RightChild = kill_node.Node.RightChild
                    scoped_node.RightChild.Parent = scoped_node
                else:
                    scoped_node.RightChild = None
                scoped_node.Parent = kill_node.Node.Parent
            else:
                if scoped_node.Parent is kill_node.Node:
                    scoped_node.LeftChild = kill_node.Node.LeftChild
                    scoped_node.Parent = kill_node.Node.Parent
                    kill_node.Node.LeftChild.Parent = scoped_node
                else:
                    scoped_node.Parent.LeftChild = scoped_node.RightChild
                    scoped_node.RightChild.Parent = scoped_node.Parent
                    scoped_node.LeftChild = kill_node.Node.LeftChild
                    scoped_node.LeftChild.Parent = scoped_node
                    scoped_node.RightChild = kill_node.Node.RightChild
                    scoped_node.RightChild.Parent = scoped_node

            if kill_node.Node.Parent.LeftChild is kill_node.Node:
                kill_node.Node.Parent.LeftChild = scoped_node
            elif kill_node.Node.Parent.RightChild is kill_node.Node:
                kill_node.Node.Parent.RightChild = scoped_node

            self.NodeCounter -= 1
            return True

    def Count(self):
        return self.NodeCounter

    def WideAllNodes(self):

        def recursive_wide_traverse(current_parents=None):
            all_nodes = []
            if current_parents is None:
                if self.Root is None:
                    return ()
                all_nodes.append(self.Root)
                current_parents = [self.Root]

            next_level_parents = []

            for parent in current_parents:
                if parent.LeftChild is not None:
                    next_level_parents.append(parent.LeftChild)
                if parent.RightChild is not None:
                    next_level_parents.append(parent.RightChild)

            all_nodes.extend(next_level_parents)

            if len(next_level_parents) > 0:
                all_nodes.extend(recursive_wide_traverse(next_level_parents))

            return all_nodes

        wide_traversed_nodes = recursive_wide_traverse()
        return tuple(wide_traversed_nodes)

    def DeepAllNodes(self, traversal_order=0):

        def traversal_inorder(parent=None):
            all_nodes = []
            if parent is None:
                if self.Root is None:
                    return []
                parent = self.Root

            if parent.LeftChild is not None:
                all_nodes.extend(traversal_inorder(parent.LeftChild))

            all_nodes.append(parent)

            if parent.RightChild is not None:
                all_nodes.extend(traversal_inorder(parent.RightChild))

            return all_nodes

        def traversal_postorder(parent=None):
            all_nodes = []
            if parent is None:
                if self.Root is None:
                    return []
                parent = self.Root

            if parent.LeftChild is not None:
                all_nodes.extend(traversal_postorder(parent.LeftChild))

            if parent.RightChild is not None:
                all_nodes.extend(traversal_postorder(parent.RightChild))

            all_nodes.append(parent)

            return all_nodes

        def traversal_preorder(parent=None):
            all_nodes = []
            if parent is None:
                if self.Root is None:
                    return []
                parent = self.Root

            all_nodes.append(parent)

            if parent.LeftChild is not None:
                all_nodes.extend(traversal_preorder(parent.LeftChild))

            if parent.RightChild is not None:
                all_nodes.extend(traversal_preorder(parent.RightChild))

            return all_nodes

        traversal_picker = {
            0: traversal_inorder,
            1: traversal_postorder,
            2: traversal_preorder
        }

        traversed_tree_nodes = traversal_picker[traversal_order]()
        return tuple(traversed_tree_nodes)



