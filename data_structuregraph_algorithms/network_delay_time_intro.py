# ---------------------------------------------------------
# Program: Network Delay Time
# Description:
# This program computes how long it takes for all nodes
# to receive a signal from a source node.
# ---------------------------------------------------------

import heapq

def network_delay_time(times, n, source):
    graph = {i: [] for i in range(1, n + 1)}

    for u, v, w in times:
        graph[u].append((v, w))

    distances = {i: float("inf") for i in range(1, n + 1)}
    distances[source] = 0

    heap = [(0, source)]

    while heap:
        current_distance, node = heapq.heappop(heap)

        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    max_distance = max(distances.values())
    return max_distance if max_distance != float("inf") else -1


times = [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1]
]

print("Network delay time:", network_delay_time(times, 4, 2))
