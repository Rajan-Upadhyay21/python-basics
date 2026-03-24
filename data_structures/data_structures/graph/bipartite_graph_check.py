# ---------------------------------------------------------
# Program: Bipartite Graph Check
# Description:
# This program checks whether a graph is bipartite using BFS.
# ---------------------------------------------------------

from collections import deque

def is_bipartite(graph):
    color = {}

    for start in graph:
        if start not in color:
            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False

    return True


graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

if is_bipartite(graph):
    print("Graph is bipartite.")
else:
    print("Graph is not bipartite.")
