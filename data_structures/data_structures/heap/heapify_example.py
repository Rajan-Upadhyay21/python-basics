# ---------------------------------------------------------
# Program: Heapify Example
# Description:
# This program converts a normal list into a heap.
# ---------------------------------------------------------

import heapq

numbers = [40, 10, 30, 20, 50, 5]

print("Original list:", numbers)

heapq.heapify(numbers)

print("Heapified list:", numbers)
print("Smallest element:", numbers[0])
