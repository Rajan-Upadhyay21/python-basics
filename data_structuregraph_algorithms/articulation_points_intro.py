# ---------------------------------------------------------
# Program: Articulation Points in Graph
# Description:
# This program finds articulation points in an undirected graph.
# ---------------------------------------------------------

def find_articulation_points(graph):
    time = [0]
    visited = set()
    discovery = {}
    low = {}
    articulation_points = set()

    def dfs(node, parent):
        visited.add(node)
        discovery[node] = low[node] = time[0]
        time[0] += 1
        children = 0

        for neighbor in graph[node]:
            if neighbor == parent:
                continue

            if neighbor not in visited:
                children += 1
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])

                if parent != -1 and low[neighbor] >= discovery[node]:
                    articulation_points.add(node)

            else:
                low[node] = min(low[node], discovery[neighbor])

        if parent == -1 and children > 1:
            articulation_points.add(node)

    for node in graph:
        if node not in visited:
            dfs(node, -1)

    return articulation_points


graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1, 4, 5],
    4: [3],
    5: [3]
}

print("Articulation points:", find_articulation_points(graph))
