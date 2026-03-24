# ---------------------------------------------------------
# Program: Graph Adjacency Matrix
# Description:
# This program demonstrates graph representation using
# an adjacency matrix.
# ---------------------------------------------------------

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

print("Graph represented as adjacency matrix:")
for row in graph:
    print(row)
