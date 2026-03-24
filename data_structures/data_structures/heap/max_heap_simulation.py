# ---------------------------------------------------------
# Program: Max Heap Simulation
# Description:
# This program demonstrates how to simulate a max-heap
# using Python's heapq by storing negative values.
# ---------------------------------------------------------

import heapq

numbers = [10, 40, 20, 5, 30]

max_heap = []

for number in numbers:
    heapq.heappush(max_heap, -number)

print("Simulated max heap:", max_heap)
print("Maximum element:", -max_heap[0])
