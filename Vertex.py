class Vertex:
    def __init__(self, id, cost, neighbours=[]):
        self.neighbours = neighbours
        self.cost = cost
        self.id = id
        self.visited = False

    def add_neighbour(self, other, cost=0):
        self.neighbours.append((other, cost))

    def remove_neighbour(self, other):
        for elem in self.neighbours:
            vertex = elem[0]
            if vertex.id == other.id:
                self.neighbours.remove(elem)

    def cost_to_visit(self, other):
        for neighbour in self.neighbours:
            if neighbour[0].id == other.id:
                return neighbour[1]

    def __str__(self):
        return str(self.id)
