# ---------------------------------------------------------
# Program: Heap Sort Intro
# Description:
# This program sorts elements using heap operations.
# ---------------------------------------------------------

import heapq

numbers = [25, 10, 40, 5, 30, 15]

print("Original list:", numbers)

heapq.heapify(numbers)

sorted_numbers = []
while numbers:
    sorted_numbers.append(heapq.heappop(numbers))

print("Sorted list using heap:", sorted_numbers)
