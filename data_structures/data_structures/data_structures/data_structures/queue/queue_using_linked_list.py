# ---------------------------------------------------------
# Program: Queue Using Linked List
# Description:
# This program demonstrates queue implementation using
# a linked list.
# ---------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def display(self):
        current = self.front
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


queue = Queue()
queue.enqueue(11)
queue.enqueue(22)
queue.enqueue(33)

print("Queue using linked list:")
queue.display()

print("Dequeued value:", queue.dequeue())
queue.display()
