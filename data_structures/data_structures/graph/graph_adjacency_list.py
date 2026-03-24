# ---------------------------------------------------------
# Program: Graph Adjacency List
# Description:
# This program demonstrates graph representation using
# an adjacency list.
# ---------------------------------------------------------

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

print("Graph represented as adjacency list:")
for node in graph:
    print(f"{node} -> {graph[node]}")
