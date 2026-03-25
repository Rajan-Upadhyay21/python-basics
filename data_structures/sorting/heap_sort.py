# ---------------------------------------------------------
# Program: Heap Sort
# Description:
# This program sorts an array using heap sort.
# It uses heap operations to repeatedly extract
# the smallest element.
# ---------------------------------------------------------

import heapq

def heap_sort(arr):
    heapq.heapify(arr)

    sorted_array = []
    while arr:
        sorted_array.append(heapq.heappop(arr))

    return sorted_array


numbers = [12, 11, 13, 5, 6, 7]

print("Original array:", numbers)
print("Sorted array:", heap_sort(numbers))
