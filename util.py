import random


def modify_solution(graph, solution):
    solution_copy = solution.copy()
    choice = random.randint(0, 3)
    # remove
    if choice == 0:
        solution_copy.remove(random.choice(solution_copy[1:-1]))
    # add
    if choice == 1:
        vertex = random.choice(graph.vertices)
        while vertex in solution_copy:
            vertex = random.choice(graph.vertices)
        index = random.randint(1, len(solution_copy) - 1)
        solution_copy.insert(index, vertex)
    # switch
    if choice == 2:
        vertex = random.choice(graph.vertices)
        while vertex in solution_copy:
            vertex = random.choice(graph.vertices)
        index = random.randint(1, len(solution_copy) - 1)

        solution_copy.remove(solution_copy[index])
        solution_copy.insert(index, vertex)
    return solution_copy


def fitness(solution):
    sum = solution[0].cost
    for i, vertex in enumerate(solution[1:]):
        sum += vertex.cost
        sum += solution[i - 1].cost_to_visit(vertex)
    return sum
