import random
import numpy as np
import pandas as pd

def get_data():
    nodes = ["Los Angeles", "Atlanta", "Miami", "New York", "Chicago", "Seattle", "Vancouver", "Toronto", "Salt Lake City", "Denver", "Dallas", "Kansas City", "Memphis", "Nashville", "Columbus", "Calgary", "Regina", "Winnipeg"]

    nodes_coordinates = {
		"Los Angeles": { "lat": 34.052235, "long": -118.24368 },
		"Atlanta": { "lat": 33.753746, "long": -84.386330 },
		"Miami": { "lat": 25.761681, "long": -80.191788 },
		"New York": { "lat": 40.730610, "long": -73.935242 },
		"Chicago": { "lat": 41.881832, "long": -87.623177 },
		"Seattle": { "lat": 47.608013, "long": -122.335167 },
		"Vancouver": { "lat": 49.246292, "long": -123.116226 },
		"Toronto": { "lat": 43.651070, "long": -79.347015 },
		"Salt Lake City": { "lat": 40.758701, "long":-111.876183 },
		"Denver": { "lat": 39.742043, "long": -104.991531 },
		"Dallas": { "lat": 32.779167, "long": -96.808891},
		"Kansas City": { "lat": 39.099724, "long": -94.578331 },
		"Memphis": { "lat": 35.117500, "long": -89.971107 },
		"Nashville": { "lat": 36.174465, "long": -86.767960 },
		"Columbus": { "lat": 39.983334, "long": -82.983330 },
		"Calgary": { "lat": 51.049999, "long": -114.066666 },
		"Regina": { "lat": 50.445210, "long": -104.618896 },
		"Winnipeg": { "lat": 49.895077, "long": -97.138451 }
	}

    cost_matrix = generate_costs(nodes_coordinates, nodes)
    return nodes, nodes_coordinates, cost_matrix
    
    
def generate_costs(nodes_coordinates, nodes):
  node_cost = []

  for x in nodes_coordinates:
    result = []
    node1 = nodes_coordinates[x]

    for y in nodes_coordinates:
      node2 = nodes_coordinates[y]

      distance = np.sqrt( (node2["lat"] - node1["lat"])  ** 2 + (node2["long"] - node1["long"]) ** 2 )
      distance = distance if distance < 30 else np.inf
      result.append(distance)

    node_cost.append(result)


  cost_matrix = pd.DataFrame(node_cost, index=nodes, columns=nodes)
  return cost_matrix


def generate_route(nodes):
  origin = random.sample(nodes, 1)[0]
  destination = random.sample(nodes, 1)[0]

  while (origin == destination):
    destination = random.sample(nodes, 1)

  return origin, destination