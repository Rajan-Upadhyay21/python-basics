# ---------------------------------------------------------
# Program: Top K Frequent Elements
# Description:
# This program finds the k most frequent elements using a heap.
# ---------------------------------------------------------

import heapq
from collections import Counter

def top_k_frequent(numbers, k):
    frequency = Counter(numbers)
    return heapq.nlargest(k, frequency.keys(), key=frequency.get)


numbers = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
k = 2

print("Numbers:", numbers)
print(f"Top {k} frequent elements:", top_k_frequent(numbers, k))
