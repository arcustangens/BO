class Graph:
    def __init__(self, vertices):
        self.vertices = vertices

    def add_vertex(self, v):
        self.vertices.append(v)

    def add_edge(self, v1, v2, cost=0):
        v1.add_neighbour(v2, cost)
        v2.add_neighbour(v1, cost)

    def remove_edge(self, v1, v2):
        v1.remove_neighbour(v2)
        v2.remove_neighbour(v1)
