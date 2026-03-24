# ---------------------------------------------------------
# Program: Linked List Insertion at Position
# Description:
# This program inserts a node at a given position in
# a linked list.
# ---------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def insert_at_position(self, position, data):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 0

        while current is not None and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            print("Invalid position.")
            return

        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(40)

print("Original linked list:")
linked_list.display()

linked_list.insert_at_position(2, 30)

print("Linked list after insertion at position 2:")
linked_list.display()
