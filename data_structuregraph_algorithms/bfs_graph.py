# ---------------------------------------------------------
# Program: Breadth-First Search (BFS)
# Description:
# This program performs BFS traversal of a graph
# starting from a given source node.
# ---------------------------------------------------------

from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

print("BFS traversal:", bfs(graph, 0))
