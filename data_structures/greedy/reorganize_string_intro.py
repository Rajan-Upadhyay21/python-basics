# ---------------------------------------------------------
# Program: Reorganize String
# Description:
# This program rearranges characters so that no two adjacent
# characters are the same, using greedy and heap logic.
# ---------------------------------------------------------

import heapq
from collections import Counter

def reorganize_string(text):
    count = Counter(text)
    max_heap = [(-freq, char) for char, freq in count.items()]
    heapq.heapify(max_heap)

    previous = (0, "")
    result = []

    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char)

        if previous[0] < 0:
            heapq.heappush(max_heap, previous)

        freq += 1
        previous = (freq, char)

    reorganized = "".join(result)
    return reorganized if len(reorganized) == len(text) else ""


text = "aab"

print("Original string:", text)
print("Reorganized string:", reorganize_string(text))
