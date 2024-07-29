from data import generate_route, get_data
from genetic import evaluate, generate_child, initial_population, mutation, tournament

POPULATION_SIZE=20
GENERATIONS=1000

current_generation = 1

nodes, nodes_coodinates, cost_matrix = get_data()
origin = "Los Angeles"
destination = "New York"


solutions = []
costs = []

population = initial_population(nodes, origin, destination, POPULATION_SIZE)

while current_generation < GENERATIONS:
	population, lowest_cost, best_solution = evaluate(population, cost_matrix)

	costs.append(lowest_cost)

	solutions.append(population[best_solution])

	print(f"Generation {current_generation} - Lowest cost: {lowest_cost} - Origin: {origin} - Destination: {destination}")

	new_population = []
	new_population.append(population[best_solution])

	while len(new_population) < POPULATION_SIZE:
		child = generate_child(population)
		for x in child:
			mutated_child = mutation(x['path'], nodes, origin, destination)
			new_population.append(x)
			new_population.append(mutated_child)

	population = new_population
	current_generation += 1
 
 
 