# ---------------------------------------------------------
# Program: Front and Rear of Queue
# Description:
# This program demonstrates how to access the front and
# rear elements of a queue.
# ---------------------------------------------------------

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)

print("Front element:", queue.front())
print("Rear element:", queue.rear())
