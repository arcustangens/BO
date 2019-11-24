import math
import random

from Graph import Graph
from Vertex import Vertex


def modify_solution(graph, solution):
    solution_copy = solution.copy()
    choice = random.randint(0, 4)
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
    # rand current path
    if choice == 3:
        random.shuffle(solution_copy[1:-1])
    return solution_copy


def fitness(solution):
    sum = solution[0].cost
    for i, vertex in enumerate(solution[1:]):
        sum += vertex.cost
        sum += solution[i - 1].cost_to_visit(vertex)
    return sum


def generate_random_point(range):
    return random.randint(range[0], range[1]), random.randint(range[0], range[1])


def generate_random(vertices_number, vertices_coordinates_range, vertex_cost_range, edge_existence_probability):
    graph = Graph([])
    for i in range(vertices_number):
        point = generate_random_point(vertices_coordinates_range)
        graph.add_vertex(Vertex(i, random.randint(vertex_cost_range[0], vertex_cost_range[1]), point[0], point[1]))

    starting_point = graph.vertices[0]

    print(str(starting_point.x) + ' ' + str(starting_point.y))

    append_realistic_edges(graph, graph.vertices, edge_existence_probability)

    return graph


def generate_custom_1(cost, probability):
    graph = Graph([])
    id = 0
    span_x = 100

    # 1 path

    v_1_num = 100
    v_1_profitability = 0.7
    for x in range(1, v_1_num):
        next_x = span_x / v_1_num * x
        graph.add_vertex(Vertex(id, round((cost / v_1_num) * v_1_profitability), next_x, random.randint(1, 10)))
        id = id + 1

    append_realistic_edges(graph, graph.vertices, probability)

    # 2 path

    path2_verticies = []
    v_2_num = 10
    v_2_profitability = 0.95
    for x in range(1, 5):
        next_x = span_x / v_2_num * x
        vertex = Vertex(id, round((cost / v_2_num) * v_2_profitability), next_x, random.randint(-15, 0))
        path2_verticies.append(vertex)
        graph.add_vertex(vertex)
        id = id + 1

    append_realistic_edges(graph, path2_verticies, probability)

    return graph


def append_realistic_edges(graph, vertices, probability):
    for v1 in vertices:
        sorted_neighbours = sorted(vertices,
                                   key=lambda p: math.sqrt((p.x - v1.x) ** 2 + (p.y - v1.y) ** 2))
        for v2 in sorted_neighbours:
            if v1.id != v2.id:
                cost = math.sqrt((v2.x - v1.x) ** 2 + (v2.y - v1.y) ** 2)
                graph.add_edge_with_probability(v1, v2, cost, probability)
