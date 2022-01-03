class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Is_hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.depth_stack = []

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

    def dfs(self, VFrom, VTo, stack_behavior=False):
        self.vertex[VFrom].Is_hit = True
        if stack_behavior:
            self.depth_stack.append(self.vertex[VFrom])

        if self.m_adjacency[VFrom][VTo] == 1:
            self.vertex[VTo].Is_hit = True
            self.depth_stack.append(self.vertex[VTo])
            return self.depth_stack
        else:
            for node, edge_check in enumerate(self.m_adjacency[VFrom]):
                if node != VFrom and edge_check == 1 and self.vertex[node].Is_hit is False:
                    return self.dfs(node, VTo, True)

        self.depth_stack.pop()

        if len(self.depth_stack) == 0:
            return []
        else:
            for i, vertex in enumerate(self.vertex):
                if vertex.Value == self.depth_stack[-1].Value:
                    return self.dfs(i, VTo)

    def DepthFirstSearch(self, VFrom, VTo):
        self.depth_stack = []
        for vertex in self.vertex:
            vertex.Is_hit = False

        return self.dfs(VFrom, VTo, True)

