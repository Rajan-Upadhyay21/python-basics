# ---------------------------------------------------------
# Program: Linked List Traversal
# Description:
# This program demonstrates traversing all nodes of a
# linked list and printing their values.
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

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


linked_list = LinkedList()
linked_list.append(5)
linked_list.append(15)
linked_list.append(25)
linked_list.append(35)

print("Traversing linked list:")
linked_list.display()
