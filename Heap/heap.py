class Heap:

    def __init__(self):
        self.HeapArray = []
        self.empty_slot_index = 0

    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * (2 ** (depth + 1) - 1)
        self.free_slot_index = 0
        for i in a:
            is_element_added = self.Add(i)
            if is_element_added is False:
                return None
        return None

    def GetMax(self):
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1

        element_to_return = self.HeapArray[0]

        current_root_index = 0
        last_existing_index = self.empty_slot_index - 1
        self.empty_slot_index = self.empty_slot_index - 1
        self.HeapArray[current_root_index] = self.HeapArray[last_existing_index]
        self.HeapArray[last_existing_index] = None

        if last_existing_index == current_root_index:
            return element_to_return

        max_child_index = current_root_index

        while True:
            current_root_index = max_child_index
            left_child_index = current_root_index * 2 + 1
            right_child_index = current_root_index * 2 + 2

            if left_child_index >= len(self.HeapArray):
                return element_to_return

            if (
                self.HeapArray[left_child_index] is not None
                and self.HeapArray[left_child_index] > self.HeapArray[max_child_index]
            ):
                max_child_index = left_child_index

            if (
                self.HeapArray[right_child_index] is not None
                and self.HeapArray[right_child_index] > self.HeapArray[max_child_index]
            ):
                max_child_index = right_child_index

            if max_child_index != current_root_index:
                self.HeapArray[current_root_index], self.HeapArray[max_child_index] = \
                    self.HeapArray[max_child_index], self.HeapArray[current_root_index]

            else:
                return element_to_return

    def Add(self, key):
        if self.empty_slot_index >= len(self.HeapArray):
            return False

        if self.HeapArray[0] is None:
            self.HeapArray[0] = key
            self.empty_slot_index = self.empty_slot_index + 1
            return True

        if self.empty_slot_index % 2 == 0:
            parent_index = (self.empty_slot_index - 2) // 2
        else:
            parent_index = (self.empty_slot_index - 1) // 2

        slot_index = self.empty_slot_index
        self.empty_slot_index = self.empty_slot_index + 1

        while parent_index >= 0 and self.HeapArray[parent_index] < key:
            self.HeapArray[slot_index] = self.HeapArray[parent_index]
            self.HeapArray[parent_index] = key

            slot_index = parent_index
            if parent_index % 2 == 0:
                parent_index = (parent_index - 2) // 2
            else:
                parent_index = (parent_index - 1) // 2
        else:
            self.HeapArray[slot_index] = key
            return True