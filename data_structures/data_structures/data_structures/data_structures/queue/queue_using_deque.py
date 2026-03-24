# ---------------------------------------------------------
# Program: Queue Using deque
# Description:
# This program demonstrates an efficient queue implementation
# using collections.deque.
# ---------------------------------------------------------

from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue operations:", list(queue))

removed_element = queue.popleft()

print("Dequeued element:", removed_element)
print("Queue after dequeue operation:", list(queue))
