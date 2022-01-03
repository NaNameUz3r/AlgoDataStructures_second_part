from simple_graph import Vertex, SimpleGraph
import unittest


class TestSimpleGraph(unittest.TestCase):
    def test_graph(self):
        simple_g = SimpleGraph(5)
        self.assertEqual(len(simple_g.m_adjacency), 5)

        simple_g.AddVertex("Hello")
        self.assertEqual(simple_g.vertex[0].Value, "Hello")
        simple_g.AddVertex("World")
        self.assertEqual(simple_g.vertex[1].Value, "World")

        self.assertEqual(simple_g.IsEdge(0, 1), False)
        simple_g.AddEdge(0, 1)
        self.assertEqual(simple_g.IsEdge(0, 1), True)

        simple_g.AddVertex("Friend")
        simple_g.AddEdge(0, 2)
        simple_g.RemoveEdge(0, 1)
        self.assertEqual(simple_g.IsEdge(0, 1), False)
        self.assertEqual(simple_g.IsEdge(0, 2), True)

        simple_g.AddEdge(0, 1)

        simple_g.RemoveVertex(0)
        self.assertEqual(simple_g.vertex[0], None)
        self.assertEqual(simple_g.IsEdge(0, 1), False)
        self.assertEqual(simple_g.IsEdge(0, 2), False)


