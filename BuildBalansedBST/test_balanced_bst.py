import unittest
from balanced_bst import GenerateBBSTArray, recursive_bst_build


class TestGenerateBBST(unittest.TestCase):
    def test_None_array(self):
        self.assertEqual(GenerateBBSTArray(None), None)
        self.assertEqual(GenerateBBSTArray([]), None)

    def test_one_element(self):
        self.assertEqual(GenerateBBSTArray([777]), [777])

    def test_base_functional(self):
        test_array = [430, 123, 943, 321, 435, 222, 101]
        print(GenerateBBSTArray(test_array))
        self.assertEqual(GenerateBBSTArray(test_array), [321, 123, 435, 101, 222, 430, 943])