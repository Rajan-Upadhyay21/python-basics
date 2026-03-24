# ---------------------------------------------------------
# Program: Task Scheduler Intro
# Description:
# This program demonstrates heap usage in a task scheduling scenario.
# ---------------------------------------------------------

import heapq

tasks = [
    (3, "Low priority task"),
    (1, "High priority task"),
    (2, "Medium priority task"),
    (4, "Very low priority task")
]

heapq.heapify(tasks)

print("Tasks executed by priority:")

while tasks:
    priority, task_name = heapq.heappop(tasks)
    print(f"Priority {priority}: {task_name}")
