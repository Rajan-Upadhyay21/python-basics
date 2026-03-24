# ---------------------------------------------------------
# Program: Circular Queue Basic
# Description:
# This program demonstrates a simple circular queue
# implementation using a fixed-size list.
# ---------------------------------------------------------

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full.")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(f"{value} added to circular queue.")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return None

        removed_value = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return removed_value

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Circular queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()

print("Dequeued value:", cq.dequeue())
cq.display()
