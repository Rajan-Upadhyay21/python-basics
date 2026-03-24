# ---------------------------------------------------------
# Program: Shortest Path in Unweighted Graph
# Description:
# This program finds the shortest path distance from a start
# node to all other nodes using BFS.
# ---------------------------------------------------------

from collections import deque

def shortest_path(graph, start):
    distance = {node: -1 for node in graph}
    distance[start] = 0

    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance


graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 5],
    4: [2, 5],
    5: [3, 4]
}

distances = shortest_path(graph, 0)

print("Shortest path distances from node 0:")
for node, dist in distances.items():
    print(f"Node {node}: {dist}")
