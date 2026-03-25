# ---------------------------------------------------------
# Program: Depth-First Search (DFS)
# Description:
# This program performs DFS traversal of a graph
# using recursion.
# ---------------------------------------------------------

def dfs(graph, node, visited=None, traversal=None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []

    visited.add(node)
    traversal.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal)

    return traversal


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

print("DFS traversal:", dfs(graph, 0))
