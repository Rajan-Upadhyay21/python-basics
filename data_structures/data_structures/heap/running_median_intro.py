# ---------------------------------------------------------
# Program: Running Median Intro
# Description:
# This program calculates the running median using two heaps.
# ---------------------------------------------------------

import heapq

class RunningMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_number(self, number):
        heapq.heappush(self.max_heap, -number)

        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)

        if len(self.max_heap) > len(self.min_heap) + 1:
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)

        if len(self.min_heap) > len(self.max_heap):
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value)

    def get_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]


stream = [5, 15, 1, 3]
median_finder = RunningMedian()

print("Running medians:")
for number in stream:
    median_finder.add_number(number)
    print(f"After inserting {number}, median is {median_finder.get_median()}")
