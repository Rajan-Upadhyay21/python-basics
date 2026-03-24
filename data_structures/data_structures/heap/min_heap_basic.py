# ---------------------------------------------------------
# Program: Min Heap Basic
# Description:
# This program demonstrates a simple min-heap using heapq.
# ---------------------------------------------------------

import heapq

heap = []

heapq.heappush(heap, 20)
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 5)

print("Min heap:", heap)
print("Smallest element:", heap[0])
