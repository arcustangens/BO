from util import modify_solution, fitness


class Bee:
    def __init__(self, graph):
        self.graph = graph
        self.randomness = 1
        self.current_solution = None

    def generate_new_solution(self):
        for i in range(self.randomness):
            new_solution = modify_solution(self.graph, self.current_solution)
            if fitness(new_solution) > fitness(self.current_solution):
                self.current_solution = new_solution
