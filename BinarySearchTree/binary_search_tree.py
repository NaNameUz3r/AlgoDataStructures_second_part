class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key, parent_node_index=0):
        # ищем в массиве индекс ключа
        if len(self.Tree) == 0:
            return None

        if parent_node_index > len(self.Tree) - 1:
            return None

        possible_node_key = self.Tree[parent_node_index]

        if possible_node_key is None:
            if parent_node_index == 0:
                return 'EmptyTree'
            else:
                return - parent_node_index

        if possible_node_key == key:
            return parent_node_index

        elif key >= possible_node_key:
            next_parent_index = 2 * parent_node_index + 2
        else:
            next_parent_index = 2 * parent_node_index + 1

        return self.FindKeyIndex(key, next_parent_index)

    def AddKey(self, key):
        # добавляем ключ в массив
        add_node_index = self.FindKeyIndex(key)
        if add_node_index is None:
            return -1

        if add_node_index == 'EmptyTree':
            add_node_index = 0
        elif add_node_index < 0:
            add_node_index = abs(add_node_index)

        if self.Tree[add_node_index] is None:
            self.Tree[add_node_index] = key
            return add_node_index
        elif self.Tree[add_node_index] == key:
            return add_node_index
        return -1

        # индекс добавленного/существующего ключа или -1 если не удалось