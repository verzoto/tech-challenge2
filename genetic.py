import random

## Gera a população inicial
def initial_population(nodes, origin, destination, POPULATION_SIZE):
  population = []
  shortest_path = {}

  # Menor caminho
  shortest_path['path'] = [origin, destination]
  population.append(shortest_path)

  for _ in range(POPULATION_SIZE):
    filtered_nodes = [node for node in nodes if node != origin and node != destination]

    individual = {}
    intermediates = random.randint(0, len(filtered_nodes))
    path = random.sample(filtered_nodes, intermediates)
    path.insert(0, origin)
    path.append(destination)
    individual['path'] = path
    population.append(individual)

  return population

# Avalia a população
def evaluate(population, cost):
  lowest_cost = None
  best_solution = None

  for index, individual in enumerate(population):
    total_cost = 0

    for location in range(len(individual['path'])-1):
      node = individual['path'][location]
      next_node = individual['path'][location+1]
      total_cost += cost.loc[node, next_node]

    # Custo total da solução
    individual['cost'] = total_cost

    if lowest_cost is None or lowest_cost > total_cost:
      lowest_cost = total_cost
      best_solution = index

  return population, lowest_cost, best_solution

# Seleciona os pais através do torneio
def tournament(population):
  parents = []
  tournament_participants = random.sample(population, 5)

  while len(parents) < 2:
    winner = min(tournament_participants, key=lambda x: x['cost'])
    tournament_participants.remove(winner)
    parents.append(winner)

  return parents

# Realiza o cruzamento
def crossover(parents):
  origin = parents[0]['path'][0]
  destination = parents[0]['path'][-1]

  parent1 = parents[0]
  parent2 = parents[1]

  length_parent1 = len(parent1)
  length_parent2 = len(parent2)

  child1 = {}
  child2 = {}

  if min(length_parent1, length_parent2) > 2:

    if min(length_parent1, length_parent2) == 3:
      index = random.randint(0, min(length_parent1, length_parent2) -2)
      path_child1 = parent1 + parent2[index:]
      path_child2 = parent2 + parent1[index:]

    else:
      index = random.randint(1, min(length_parent1, length_parent2) - 2)
      path_child1 = parent1[:index] + parent2[index:]
      path_child2 = parent2[:index] + parent1[index:]

    path_child1 = fix_path(path_child1, origin, destination)
    path_child2 = fix_path(path_child2, origin, destination)

    child1['path'] = path_child1
    child2['path'] = path_child2

    return [child1, child2]

  else:
    return parents


# Realiza a mutação
def mutation(path, nodes, origin, destination):
  mutated_path = path.copy()
  length = len(mutated_path)
  filtered_nodes = [node for node in nodes if node != origin and node != destination]

  if length == 2 or length == 3:
    node_chosen = random.sample(filtered_nodes, 1)
    mutated_path.insert(1, node_chosen[0])
  
  elif length > 3:
    mutated_path.pop(random.randint(1, length-1))

  mutated_path = fix_path(mutated_path, origin, destination)
  mutated = {}
  mutated['path'] = mutated_path

  return mutated


def generate_child(population):
    parents = tournament(population)
    child = crossover(parents)
    return child
  
def fix_path(path, origin, destination):

  if (path[0] != origin):
    path[0] = origin

  if (path[-1] != destination):
    path[-1] = destination

  path = list(dict.fromkeys(path))
  
  return path