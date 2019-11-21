import random

from Bee import Bee
from Vertex import Vertex
from Graph import Graph
from util import modify_solution, fitness

graph = Graph([])
for i in range(100):
    graph.add_vertex(Vertex(i, random.randint(15, 60)))

for v1 in graph.vertices:
    for v2 in graph.vertices:
        if v1.id != v2.id:
            graph.add_edge(v1, v2, random.randint(10, 30))

cost = 1000

v = random.choice(graph.vertices)
current_cost = v.cost
v0 = v
path = [v0]

while current_cost < cost:
    next = random.choice(v.neighbours)
    while next[0] in path:
        next = random.choice(v.neighbours)
    path.append(next[0])
    v = next[0]
    current_cost += next[1] + next[0].cost
    # print(v.id, "  ", v.cost, "  ", next[1])

n_of_bees = 100
n_of_good = 20
n_of_elite = 10
good_solutions = 10
elite_solutions = 5

bees = [Bee(graph) for x in range(0, n_of_bees)]
best_solution = None
iteration = 0
for bee in bees:
    bee.current_solution = modify_solution(graph, path)

all_time_best_solution = path

for i in range(200):
    solutions = [bee.current_solution for bee in bees]
    fitnesses = [fitness(solution) for solution in solutions]
    fit_sol = list(zip(fitnesses, solutions))
    fit_sol.sort(key=lambda x: x[0])

    current_best_solution = fit_sol[-1][1]
    if fitness(current_best_solution) > fitness(all_time_best_solution):
        all_time_best_solution = current_best_solution

    # sort solutions and assign bees
    elite_sols = [s for (f, s) in fit_sol[:elite_solutions]]
    good_sols = [s for (f, s) in fit_sol[elite_solutions:good_solutions]]
    rest_sols = [s for (f, s) in fit_sol[good_solutions:]]
    for i, bee in enumerate(bees[:n_of_elite]):
        bee.current_solution = elite_sols[i % len(elite_sols)]
    for i, bee in enumerate(bees[n_of_elite:n_of_good]):
        bee.current_solution = good_sols[i % len(good_sols)]
        bee.randomness = 2
    for i, bee in enumerate(bees[n_of_good:]):
        bee.current_solution = rest_sols[i % len(rest_sols)]
        bee.randomness = 5

    # generate new solutions
    for bee in bees:
        bee.generate_new_solution()

    print(fitness(current_best_solution))
