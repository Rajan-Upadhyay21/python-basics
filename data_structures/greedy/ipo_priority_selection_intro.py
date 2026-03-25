# ---------------------------------------------------------
# Program: IPO Project Selection
# Description:
# This program selects at most k projects to maximize capital
# using greedy selection with heaps.
# ---------------------------------------------------------

import heapq

def find_maximized_capital(k, initial_capital, profits, capital):
    projects = list(zip(capital, profits))
    projects.sort()

    max_heap = []
    current_capital = initial_capital
    index = 0

    for _ in range(k):
        while index < len(projects) and projects[index][0] <= current_capital:
            heapq.heappush(max_heap, -projects[index][1])
            index += 1

        if not max_heap:
            break

        current_capital += -heapq.heappop(max_heap)

    return current_capital


k = 2
initial_capital = 0
profits = [1, 2, 3]
capital = [0, 1, 1]

print("Maximum capital after project selection:",
      find_maximized_capital(k, initial_capital, profits, capital))
