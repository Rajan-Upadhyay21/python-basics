# ---------------------------------------------------------
# Program: Queue Operations
# Description:
# This program demonstrates enqueue, dequeue, and display
# operations using a custom queue class.
# ---------------------------------------------------------

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)
        print(f"{value} added to queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Current queue:", self.items)


queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.display()

print("Dequeued value:", queue.dequeue())
queue.display()
