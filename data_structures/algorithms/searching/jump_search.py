# ---------------------------------------------------------
# Program: Jump Search
# Description:
# This program searches for a target element in a sorted
# array using jump search.
# ---------------------------------------------------------

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1

    return -1


numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 15

result = jump_search(numbers, target)

print("Sorted array:", numbers)
print("Target:", target)
print("Result index:", result)
