import unittest

from heap import Heap


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_depth(self):
        self.heap = Heap()
        self.heap.MakeHeap([5], 0)
        self.assertEqual(len(self.heap.HeapArray), 1)

        self.heap = Heap()
        self.heap.MakeHeap([65, 43, 44], 1)
        self.assertEqual(len(self.heap.HeapArray), 3)

        self.heap = Heap()
        self.heap.MakeHeap([1, 2, 3, 4, 5, 6, 7], 2)
        self.assertEqual(len(self.heap.HeapArray), 7)

        self.heap = Heap()
        self.heap.MakeHeap([1, 2, 3, 4, 5], 1)
        self.assertEqual(len(self.heap.HeapArray), 3)
        self.assertEqual(self.heap.HeapArray, [3, 1, 2])

    def test_add(self):
        self.heap = Heap()
        self.heap.MakeHeap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)
        self.assertEqual(len(self.heap.HeapArray), 15)
        self.assertEqual(self.heap.Add(10), True)
        self.assertEqual(len(self.heap.HeapArray), 15)
        self.assertEqual(self.heap.HeapArray, [11, 10, 4, 7, 9, 3, 1, 2, 5, 6, 8, None, None, None, None])

        self.assertEqual(self.heap.Add(40), True)
        self.assertEqual(self.heap.HeapArray, [40, 10, 11, 7, 9, 4, 1, 2, 5, 6, 8, 3, None, None, None])

        self.assertEqual(self.heap.Add(13), True)
        self.assertEqual(self.heap.HeapArray, [40, 10, 13, 7, 9, 11, 1, 2, 5, 6, 8, 3, 4, None, None])

        self.assertEqual(self.heap.Add(14), True)
        self.assertEqual(self.heap.HeapArray, [40, 10, 14, 7, 9, 11, 13, 2, 5, 6, 8, 3, 4, 1, None])

        self.assertEqual(self.heap.Add(15), True)
        self.assertEqual(self.heap.HeapArray, [40, 10, 15, 7, 9, 11, 14, 2, 5, 6, 8, 3, 4, 1, 13])

        self.assertEqual(self.heap.Add(123412341234), False)
        self.assertEqual(self.heap.HeapArray, [40, 10, 15, 7, 9, 11, 14, 2, 5, 6, 8, 3, 4, 1, 13])


    def test_get_max(self):
        self.heap = Heap()
        self.heap.MakeHeap([1], 0)
        self.assertEqual(self.heap.GetMax(), 1)
        self.assertEqual(self.heap.GetMax(), -1)

        self.heap = Heap()
        self.heap.MakeHeap([500, 39, 45, 13, 11, 6, 7, 999, 564], 3)
        self.assertEqual(self.heap.HeapArray, [999, 564, 45, 500, 11, 6, 7, 13, 39, None, None, None, None, None, None])
        self.assertEqual(self.heap.GetMax(), 999)
        self.assertEqual(self.heap.HeapArray, [564, 500, 45, 39, 11, 6, 7, 13, None, None, None, None, None, None, None])

        self.heap = Heap()
        self.heap.MakeHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3)

        self.assertEqual(self.heap.GetMax(), 11)
        self.assertEqual(self.heap.HeapArray, [10, 9, 6, 7, 8, 2, 5, 1, 4, 3, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 10)
        self.assertEqual(self.heap.HeapArray, [9, 8, 6, 7, 3, 2, 5, 1, 4, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 9)
        self.assertEqual(self.heap.HeapArray, [8, 7, 6, 4, 3, 2, 5, 1, None, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 8)
        self.assertEqual(self.heap.HeapArray, [7, 4, 6, 1, 3, 2, 5, None, None, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 7)
        self.assertEqual(self.heap.HeapArray, [6, 4, 5, 1, 3, 2,None, None, None, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 6)
        self.assertEqual(self.heap.HeapArray, [5, 4, 2, 1, 3, None, None, None, None, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 5)
        self.assertEqual(self.heap.GetMax(), 4)
        self.assertEqual(self.heap.GetMax(), 3)
        self.assertEqual(self.heap.HeapArray, [2, 1, None, None, None, None, None, None, None, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 2)
        self.assertEqual(self.heap.HeapArray, [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), 1)
        self.assertEqual(self.heap.HeapArray, [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])

        self.assertEqual(self.heap.GetMax(), -1)
        self.assertEqual(self.heap.HeapArray,  [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
