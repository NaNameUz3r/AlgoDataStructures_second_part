class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

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

    def WeakVertices(self):
        intersection_map = {}
        for vertex in range(len(self.vertex)):
            intersection_map[str(vertex)] = []
            for vertex_index in range(self.max_vertex):
                if self.m_adjacency[vertex][vertex_index] == 1:
                    intersection_map[str(vertex)].append(vertex_index)
        weak_vertex = []
        for vertex_key in intersection_map.keys():
            strong_edges = 0
            for adjacent_vertex in intersection_map[vertex_key]:
                adjacent_vertex_crossings = set(intersection_map[str(adjacent_vertex)])
                if len(adjacent_vertex_crossings.intersection(intersection_map[vertex_key])) > 0:
                    strong_edges += 1
                    break
            if strong_edges == 0:
                weak_vertex.append(self.vertex[int(vertex_key)])
        return weak_vertex
