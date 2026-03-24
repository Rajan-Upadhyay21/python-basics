# ---------------------------------------------------------
# Program: Connected Components
# Description:
# This program counts connected components in an undirected graph.
# ---------------------------------------------------------

def dfs(graph, node, visited):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def count_connected_components(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            count += 1

    return count


graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}

print("Number of connected components:", count_connected_components(graph))
