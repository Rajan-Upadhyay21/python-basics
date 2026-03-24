# ---------------------------------------------------------
# Program: Sort Nearly Sorted Array
# Description:
# This program sorts an array where every element is at most
# k positions away from its target position.
# ---------------------------------------------------------

import heapq

def sort_nearly_sorted_array(arr, k):
    heap = arr[:k + 1]
    heapq.heapify(heap)

    target_index = 0

    for i in range(k + 1, len(arr)):
        arr[target_index] = heapq.heappop(heap)
        heapq.heappush(heap, arr[i])
        target_index += 1

    while heap:
        arr[target_index] = heapq.heappop(heap)
        target_index += 1

    return arr


numbers = [6, 5, 3, 2, 8, 10, 9]
k = 3

print("Original array:", numbers)
print("Sorted array:", sort_nearly_sorted_array(numbers, k))
