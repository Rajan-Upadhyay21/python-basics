# ---------------------------------------------------------
# Program: Cycle Detection in Undirected Graph
# Description:
# This program checks whether an undirected graph contains a cycle.
# ---------------------------------------------------------

def has_cycle(graph, node, visited, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True

    return False


def detect_cycle(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            if has_cycle(graph, node, visited, -1):
                return True

    return False


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

if detect_cycle(graph):
    print("Cycle detected in graph.")
else:
    print("No cycle detected.")
