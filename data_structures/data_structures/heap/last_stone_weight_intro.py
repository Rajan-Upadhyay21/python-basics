# ---------------------------------------------------------
# Program: Last Stone Weight
# Description:
# This program simulates the last stone weight problem
# using a max-heap.
# ---------------------------------------------------------

import heapq

def last_stone_weight(stones):
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        stone1 = -heapq.heappop(max_heap)
        stone2 = -heapq.heappop(max_heap)

        if stone1 != stone2:
            heapq.heappush(max_heap, -(stone1 - stone2))

    return -max_heap[0] if max_heap else 0


stones = [2, 7, 4, 1, 8, 1]

print("Stones:", stones)
print("Last stone weight:", last_stone_weight(stones))
