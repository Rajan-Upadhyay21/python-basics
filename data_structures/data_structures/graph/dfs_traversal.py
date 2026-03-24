# ---------------------------------------------------------
# Program: Depth-First Search (DFS)
# Description:
# This program demonstrates DFS traversal of a graph
# using recursion.
# ---------------------------------------------------------

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

visited = set()

print("DFS traversal starting from node 0:")
dfs(graph, 0, visited)
