import random


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices

    def add_vertex(self, v):
        self.vertices.append(v)

    def add_edge_with_probability(self, v1, v2, cost, probability):
        rand = random.randint(round((1 - probability) * -10), round(probability * 10))
        if rand > 0:
            self.add_edge(v1, v2, cost)
            print('Added edge with cost ' + str(cost))
        else:
            print('Too bad!')

    def add_edge(self, v1, v2, cost=0):
        v1.add_neighbour(v2, cost)

    def remove_edge(self, v1, v2):
        v1.remove_neighbour(v2)
        v2.remove_neighbour(v1)
