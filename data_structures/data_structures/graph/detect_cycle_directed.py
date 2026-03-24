# ---------------------------------------------------------
# Program: Cycle Detection in Directed Graph
# Description:
# This program checks whether a directed graph contains a cycle.
# ---------------------------------------------------------

def dfs(node, graph, visited, recursion_stack):
    visited.add(node)
    recursion_stack.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, graph, visited, recursion_stack):
                return True
        elif neighbor in recursion_stack:
            return True

    recursion_stack.remove(node)
    return False


def has_cycle(graph):
    visited = set()
    recursion_stack = set()

    for node in graph:
        if node not in visited:
            if dfs(node, graph, visited, recursion_stack):
                return True

    return False


graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]
}

if has_cycle(graph):
    print("Cycle detected in directed graph.")
else:
    print("No cycle detected.")
