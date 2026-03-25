# ---------------------------------------------------------
# Program: Course Schedule using Topological Sort
# Description:
# This program checks whether all courses can be completed
# using topological sorting.
# ---------------------------------------------------------

from collections import deque

def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    indegree = {i: 0 for i in range(num_courses)}

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([course for course in indegree if indegree[course] == 0])
    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses


num_courses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]

print("Can finish all courses:", can_finish(num_courses, prerequisites))
