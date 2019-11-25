import random

from Bee import Bee
from util import modify_solution, fitness, generate_random

vertex_cost_range = (15, 60)
edge_cost_range = (15, 60)
edge_existence_probability = 0.9
vertices_coordinates_range = (0, 50)
vertices_number = 100
cost = 1000

graph = generate_random(vertices_number, vertices_coordinates_range, vertex_cost_range, edge_existence_probability)


v = random.choice(graph.vertices)
current_cost = v.cost
v0 = v
path = [v0]

while current_cost < cost:
    next = random.choice(v.neighbours)
    while next[0] in path:
        next = random.choice(v.neighbours)

    while not v.is_neighbour_with(next[0]):
        next = random.choice(v.neighbours)
        while next[0] in path:
            next = random.choice(v.neighbours)
    print(str(path[-1].id) + ' ' + str(next[0].id))
    path.append(next[0])
    v = next[0]
    current_cost += next[1] + next[0].cost

n_of_bees = 100
n_of_good = 20
n_of_elite = 10
good_solutions = 10
elite_solutions = 5
max_best_solution_len = round(vertices_number / 3)

bees = [Bee(graph) for x in range(0, n_of_bees)]
best_solution = None
iteration = 0
for bee in bees:
    bee.current_solution = modify_solution(graph, path)

all_time_best_solution = path


for i in range(20):
    solutions = [bee.current_solution for bee in bees]
    fitnesses = [fitness(solution) for solution in solutions]
    fit_sol = list(zip(fitnesses, solutions))
    fit_sol.sort(key=lambda x: x[0])

    current_best_solution = fit_sol[-1][1]
    if fitness(current_best_solution) > fitness(all_time_best_solution) and len(current_best_solution) < max_best_solution_len:
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

    print('Fitness: ' + str(fitness(current_best_solution)) + ' Length of path: ' + str(len(current_best_solution)))


# for i, v in enumerate(all_time_best_solution):
#     print(str(all_time_best_solution[i]))

