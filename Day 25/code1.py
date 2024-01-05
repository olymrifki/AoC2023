filename = "./Day 25/data.txt"

import random
from math import prod

import networkx as nx

G = nx.Graph()

with open(filename) as file:
    for line in file.readlines():
        line = line.strip()
        node, neighbours = line.split(": ")
        for neighbour in neighbours.split(" "):
            G.add_edge(node, neighbour)

freq = {}
nodes = list(G.nodes)
for i in range(1000):
    node1 = random.choice(nodes)
    node2 = random.choice(nodes)
    path = nx.shortest_path(G, node1, node2)
    for i in range(len(path[1:])):
        freq[((path[i + 1], path[i]))] = freq.get(((path[i + 1], path[i])), 0) + 1
        freq[((path[i], path[i + 1]))] = freq.get(((path[i], path[i + 1])), 0) + 1

hotest_nodes = [
    res[0] for res in sorted(list(freq.items()), key=lambda i: i[1], reverse=True)[:6:2]
]
print(hotest_nodes)
G.remove_edges_from(hotest_nodes)
print(prod([len(c) for c in nx.connected_components(G)]))
