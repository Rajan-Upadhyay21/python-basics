# ---------------------------------------------------------
# Program: Detect Cycle in Directed Graph
# Description:
# This program checks whether a directed graph
# contains a cycle using DFS.
# ---------------------------------------------------------

def dfs_cycle(node, graph, visited, recursion_stack):
    visited.add(node)
    recursion_stack.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_cycle(neighbor, graph, visited, recursion_stack):
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
            if dfs_cycle(node, graph, visited, recursion_stack):
                return True

    return False


graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]
}

print("Cycle exists in directed graph:", has_cycle(graph))
