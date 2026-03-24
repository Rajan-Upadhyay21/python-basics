# ---------------------------------------------------------
# Program: Connect Ropes with Minimum Cost
# Description:
# This program finds the minimum cost to connect all ropes
# using a min-heap.
# ---------------------------------------------------------

import heapq

def min_cost_to_connect_ropes(ropes):
    heapq.heapify(ropes)
    total_cost = 0

    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)

        cost = first + second
        total_cost += cost

        heapq.heappush(ropes, cost)

    return total_cost


ropes = [4, 3, 2, 6]

print("Rope lengths:", ropes)
print("Minimum total cost:", min_cost_to_connect_ropes(ropes))
