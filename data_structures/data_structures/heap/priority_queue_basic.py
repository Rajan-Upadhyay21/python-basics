# ---------------------------------------------------------
# Program: Priority Queue Basic
# Description:
# This program demonstrates a priority queue using heapq.
# Smaller priority number means higher priority.
# ---------------------------------------------------------

import heapq

tasks = []

heapq.heappush(tasks, (2, "Write report"))
heapq.heappush(tasks, (1, "Fix urgent bug"))
heapq.heappush(tasks, (3, "Reply to emails"))

print("Tasks in priority order:")

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Priority {priority}: {task}")
