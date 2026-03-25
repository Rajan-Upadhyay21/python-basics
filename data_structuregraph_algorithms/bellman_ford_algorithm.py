# ---------------------------------------------------------
# Program: Bellman-Ford Algorithm
# Description:
# This program finds shortest paths from a source node
# and also detects negative weight cycles.
# ---------------------------------------------------------

def bellman_ford(vertices, edges, source):
    distances = {vertex: float("inf") for vertex in range(vertices)}
    distances[source] = 0

    for _ in range(vertices - 1):
        for u, v, weight in edges:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    for u, v, weight in edges:
        if distances[u] != float("inf") and distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle.")
            return None

    return distances


vertices = 5
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

print("Bellman-Ford shortest distances from source 0:")
print(bellman_ford(vertices, edges, 0))
