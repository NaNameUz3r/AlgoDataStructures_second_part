import unittest
from weak_vertices import Vertex, SimpleGraph


class Test(unittest.TestCase):
    def test_empty_list(self):
        self.size = 0
        self.test_graph = SimpleGraph(self.size)
        self.assertEqual(self.test_graph.WeakVertices(), [])

    def test_loop(self):
        self.size = 5
        self.test_graph = SimpleGraph(self.size)
        self.test_graph.AddVertex("H")
        self.test_graph.AddVertex("E")
        self.test_graph.AddVertex("L")
        self.test_graph.AddVertex("L")
        self.test_graph.AddVertex("O")
        self.test_graph.AddEdge(0, 1)
        self.test_graph.AddEdge(0, 2)
        self.test_graph.AddEdge(1, 3)
        self.test_graph.AddEdge(2, 3)
        self.test_graph.AddEdge(3, 4)
        self.assertEqual(
            self.test_graph.m_adjacency,
            [
                [0, 1, 1, 0, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [0, 1, 1, 0, 1],
                [0, 0, 0, 1, 0]
            ],
        )

        self.assertEqual([vertex.Value for vertex in self.test_graph.WeakVertices()], ['H', 'E', 'L', 'L', 'O'])

        self.test_graph.AddEdge(2, 1)
        self.assertEqual(
            self.test_graph.m_adjacency,
            [
                [0, 1, 1, 0, 0],
                [1, 0, 1, 1, 0],
                [1, 1, 0, 1, 0],
                [0, 1, 1, 0, 1],
                [0, 0, 0, 1, 0]
            ],
        )

        self.assertEqual([vertex.Value for vertex in self.test_graph.WeakVertices()], ['O'])
