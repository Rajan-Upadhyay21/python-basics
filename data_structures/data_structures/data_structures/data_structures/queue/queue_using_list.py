# ---------------------------------------------------------
# Program: Queue Using List
# Description:
# This program demonstrates a simple queue implementation
# using a Python list.
# ---------------------------------------------------------

queue = []

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue operations:", queue)

# Dequeue element
removed_element = queue.pop(0)

print("Dequeued element:", removed_element)
print("Queue after dequeue operation:", queue)
