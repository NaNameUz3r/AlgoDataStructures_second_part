class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def represent_tree_as_list(self, parent=None):
        nodes_list = []
        if parent is None:
            nodes_list.append(self.Root.NodeKey)
            parent = self.Root
        else:
            nodes_list.append(parent.NodeKey)

        if parent.LeftChild is not None:
            nodes_list.extend(self.represent_tree_as_list(parent.LeftChild))
        if parent.RightChild is not None:
            nodes_list.extend(self.represent_tree_as_list(parent.RightChild))

        return nodes_list

    def recursive_build_tree(self, parent, array):
        array_length = len(array)
        array_middle = array_length // 2

        node_created = BSTNode(key=array[array_middle], parent=parent)
        node_created.Level = parent.Level + 1

        left_subtree = array[0:array_middle]
        if array_middle > array_length:
            right_subtree = array[array_middle:]
        else:
            right_subtree = array[array_middle+1:]

        if len(left_subtree) >= 1:
            node_created.LeftChild = self.recursive_build_tree(node_created, left_subtree)
            node_created.LeftChild.Level = node_created.Level + 1

        if len(right_subtree) >= 1:
            node_created.RightChild = self.recursive_build_tree(node_created, right_subtree)
            node_created.RightChild.Level = node_created.Level + 1

        return node_created

    def GenerateTree(self, a):
        if not a:
            return None

        array_length = len(a)
        array_middle = array_length // 2

        if array_length == 1:
            self.Root = BSTNode(key=a[0], parent=None)
            self.Root.Level = 0
            return None

        sorted_input_array = sorted(a)
        self.Root = BSTNode(key=sorted_input_array[array_middle], parent=None)
        self.Root.Level = 0

        left_subtree = sorted_input_array[0:array_middle]
        if array_middle > array_length:
            right_subtree = sorted_input_array[array_middle:]
        else:
            right_subtree = sorted_input_array[array_middle+1:]

        self.Root.LeftChild = self.recursive_build_tree(parent=self.Root, array=left_subtree)
        self.Root.RightChild = self.recursive_build_tree(parent=self.Root, array=right_subtree)

    def recursive_depth_check(self, node):
        current_depth = node.Level
        if node.LeftChild is not None:
            if node.LeftChild.NodeKey > node.NodeKey:
                return -1
            new_depth = self.recursive_depth_check(node.LeftChild)
            if new_depth > current_depth:
                current_depth = new_depth

        if node.RightChild is not None:
            if node.RightChild.NodeKey < node.NodeKey:
                return -1
            new_depth = self.recursive_depth_check(node.RightChild)
            if new_depth > current_depth:
                current_depth = new_depth
        return current_depth

    def IsBalanced(self, root_node):
        if root_node is None:
            return True

        if root_node.LeftChild is None:
            left_depth = root_node.Level
        else:
            left_depth = self.recursive_depth_check(root_node.LeftChild)

        if root_node.RightChild is None:
            right_depth = root_node.Level
        else:
            right_depth = self.recursive_depth_check(root_node.RightChild)

        if left_depth == -1 or right_depth == -1:
            return False

        return abs(left_depth - right_depth) <= 1
