import unittest
from depth_first_search import Vertex, SimpleGraph


class Test(unittest.TestCase):
    def test_DepthFirstSearch2(self):

        self.size = 10
        self.test_graph = SimpleGraph(self.size)
        self.test_graph.AddVertex("H")
        self.test_graph.AddVertex("E")
        self.test_graph.AddVertex("L")
        self.test_graph.AddVertex("L")
        self.test_graph.AddVertex("O")
        self.test_graph.AddVertex("W")
        self.test_graph.AddVertex("O")
        self.test_graph.AddVertex("R")
        self.test_graph.AddVertex("L")
        self.test_graph.AddVertex("D")

        self.assertEqual(self.test_graph.m_adjacency, [[0] * self.size for _ in range(self.size)])
        self.test_graph.AddEdge(0, 6)
        self.test_graph.AddEdge(0, 1)
        self.test_graph.AddEdge(6, 1)
        self.test_graph.AddEdge(3, 1)
        self.test_graph.AddEdge(9, 4)
        self.test_graph.AddEdge(9, 2)
        self.test_graph.AddEdge(2, 7)
        self.test_graph.AddEdge(2, 3)
        self.test_graph.AddEdge(2, 0)
        self.test_graph.AddEdge(5, 1)
        self.assertEqual(
            self.test_graph.m_adjacency,
            [
                [0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                [1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
                [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
            ],
        )

        first_test = self.test_graph.DepthFirstSearch(0, 4)
        self.assertEqual([x.Value for x in first_test], ['H', 'E', 'L', 'L', 'D', 'O'])

        second_test = self.test_graph.DepthFirstSearch(3, 9)
        self.assertEqual([x.Value for x in second_test], ['L', 'E', 'H', 'L', 'D'])

        third_test = self.test_graph.DepthFirstSearch(2, 6)
        self.assertEqual([x.Value for x in third_test], ['L', 'H', 'O'])

        fourth_test = self.test_graph.DepthFirstSearch(9, 1)
        self.assertEqual([x.Value for x in fourth_test], ['D', 'L', 'H', 'E'])

        # ⣿⣿⣿⣿⣿⣿⠿⢋⣥⣴⣶⣶⣶⣬⣙⠻⠟⣋⣭⣭⣭⣭⡙⠻⣿⣿⣿⣿⣿
        # ⣿⣿⣿⣿⡿⢋⣴⣿⣿⠿⢟⣛⣛⣛⠿⢷⡹⣿⣿⣿⣿⣿⣿⣆⠹⣿⣿⣿⣿
        # ⣿⣿⣿⡿⢁⣾⣿⣿⣴⣿⣿⣿⣿⠿⠿⠷⠥⠱⣶⣶⣶⣶⡶⠮⠤⣌⡙⢿⣿
        # ⣿⡿⢛⡁⣾⣿⣿⣿⡿⢟⡫⢕⣪⡭⠥⢭⣭⣉⡂⣉⡒⣤⡭⡉⠩⣥⣰⠂⠹
        # ⡟⢠⣿⣱⣿⣿⣿⣏⣛⢲⣾⣿⠃⠄⠐⠈⣿⣿⣿⣿⣿⣿⠄⠁⠃⢸⣿⣿⡧
        # ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣇⣊⠙⠳⠤⠤⠾⣟⠛⠍⣹⣛⣛⣢⣀⣠⣛⡯⢉⣰
        # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⠶⢒⣠⣼⣿⣿⣛⠻⠛⢛⣛⠉⣴⣿⣿
        # ⣿⣿⣿⣿⣿⣿⣿⡿⢛⡛⢿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⢿⣿
        # ⣿⣿⣿⣿⣿⣿⣿⠸⣿⡻⢷⣍⣛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢇⡘⣿
        # ⣿⣿⣿⣿⣿⣿⣿⣷⣝⠻⠶⣬⣍⣛⣛⠓⠶⠶⠶⠤⠬⠭⠤⠶⠶⠞⠛⣡⣿
        # ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣬⣭⣍⣙⣛⣛⣛⠛⠛⠛⠿⠿⠿⠛⣠⣿⣿
        # ⣦⣈⠉⢛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⣁⣴⣾⣿⣿⣿⣿
        # ⣿⣿⣿⣶⣮⣭⣁⣒⣒⣒⠂⠠⠬⠭⠭⠭⢀⣀⣠⣄⡘⠿⣿⣿⣿⣿⣿⣿⣿
        # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿⣿⣿
