# ---------------------------------------------------------
# Program: Strongly Connected Components (Kosaraju)
# Description:
# This program finds SCCs in a directed graph
# using Kosaraju's algorithm.
# ---------------------------------------------------------

def dfs_fill(node, graph, visited, stack):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_fill(neighbor, graph, visited, stack)

    stack.append(node)


def dfs_collect(node, graph, visited, component):
    visited.add(node)
    component.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_collect(neighbor, graph, visited, component)


def reverse_graph(graph):
    reversed_graph = {node: [] for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)

    return reversed_graph


def kosaraju(graph):
    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            dfs_fill(node, graph, visited, stack)

    reversed_graph = reverse_graph(graph)
    visited.clear()
    sccs = []

    while stack:
        node = stack.pop()

        if node not in visited:
            component = []
            dfs_collect(node, reversed_graph, visited, component)
            sccs.append(component)

    return sccs


graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: []
}

print("Strongly connected components:")
print(kosaraju(graph))
