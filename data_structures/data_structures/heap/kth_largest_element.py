# ---------------------------------------------------------
# Program: Kth Largest Element
# Description:
# This program finds the kth largest element using a heap.
# ---------------------------------------------------------

import heapq

def find_kth_largest(numbers, k):
    return heapq.nlargest(k, numbers)[-1]


numbers = [7, 10, 4, 3, 20, 15]
k = 3

print("Numbers:", numbers)
print(f"{k}rd largest element:", find_kth_largest(numbers, k))
