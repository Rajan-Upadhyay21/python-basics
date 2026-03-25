# ---------------------------------------------------------
# Program: Bridges in Graph
# Description:
# This program finds all bridges in an undirected graph.
# ---------------------------------------------------------

def find_bridges(graph):
    time = [0]
    visited = set()
    discovery = {}
    low = {}
    bridges = []

    def dfs(node, parent):
        visited.add(node)
        discovery[node] = low[node] = time[0]
        time[0] += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue

            if neighbor not in visited:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])

                if low[neighbor] > discovery[node]:
                    bridges.append((node, neighbor))
            else:
                low[node] = min(low[node], discovery[neighbor])

    for node in graph:
        if node not in visited:
            dfs(node, -1)

    return bridges


graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1, 4],
    4: [3]
}

print("Bridges in graph:", find_bridges(graph))
