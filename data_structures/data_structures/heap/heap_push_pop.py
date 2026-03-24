# ---------------------------------------------------------
# Program: Heap Push and Pop
# Description:
# This program demonstrates insertion and removal
# of elements from a heap.
# ---------------------------------------------------------

import heapq

heap = []

heapq.heappush(heap, 15)
heapq.heappush(heap, 10)
heapq.heappush(heap, 25)
heapq.heappush(heap, 5)

print("Heap after insertions:", heap)

removed = heapq.heappop(heap)
print("Removed smallest element:", removed)
print("Heap after removal:", heap)
