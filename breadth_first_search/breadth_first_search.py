class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Is_hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.search_queue = []
        self.found_path = {}

    def AddVertex(self, v):
        new_vertex = Vertex(v)
        if None in self.vertex:
            new_vertex_index = self.vertex.index(None)
            self.vertex[new_vertex_index] = new_vertex
        else:
            return None

    def RemoveVertex(self, v):
        self.vertex[v] = None
        for row in self.m_adjacency:
            row[v] = 0
        self.m_adjacency[v] = [0] * self.max_vertex

    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def __lead_the_way(self, path_loop=False):
        starting_node = list(self.found_path.keys())[0]
        path_container = [list(self.found_path.keys())[-1]]
        while path_container[-1] != starting_node:
            path_container.append(self.found_path[path_container[-1]])
        path_container.reverse()
        if path_loop:
            path_container.append(starting_node)
        return [self.vertex[i] for i in path_container]

    def __bfs(self, VFrom, VTo):
        self.vertex[VFrom].Is_hit = True

        if self.m_adjacency[VFrom][VTo] == 1:
            self.vertex[VTo].Is_hit = True
            if VTo not in self.found_path:
                self.found_path[VTo] = VFrom
                return self.__lead_the_way(False)
            else:
                return self.__lead_the_way(True)

        else:
            for node, edge_check in enumerate(self.m_adjacency[VFrom]):
                if node != VFrom and edge_check == 1 and self.vertex[node].Is_hit is False:
                    if node not in self.search_queue:
                        self.search_queue.append(node)
                        self.found_path[node] = VFrom
            self.search_queue.pop(0)

            if len(self.search_queue) == 0:
                return []

            return self.__bfs(self.search_queue[0], VTo)

    def BreadthFirstSearch(self, VFrom, VTo):
        self.search_queue = []
        self.found_path = {}
        for vertex in self.vertex:
            vertex.Is_hit = False
        self.search_queue.append(VFrom)
        self.found_path[VFrom] = None
        return self.__bfs(VFrom, VTo)