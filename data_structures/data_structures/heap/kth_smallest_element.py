# ---------------------------------------------------------
# Program: Kth Smallest Element
# Description:
# This program finds the kth smallest element using a heap.
# ---------------------------------------------------------

import heapq

def find_kth_smallest(numbers, k):
    return heapq.nsmallest(k, numbers)[-1]


numbers = [7, 10, 4, 3, 20, 15]
k = 2

print("Numbers:", numbers)
print(f"{k}nd smallest element:", find_kth_smallest(numbers, k))
