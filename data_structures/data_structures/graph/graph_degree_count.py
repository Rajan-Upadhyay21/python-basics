# ---------------------------------------------------------
# Program: Graph Degree Count
# Description:
# This program calculates the degree of each node
# in an undirected graph.
# ---------------------------------------------------------

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1]
}

print("Degree of each node:")
for node in graph:
    print(f"Node {node}: Degree {len(graph[node])}")
