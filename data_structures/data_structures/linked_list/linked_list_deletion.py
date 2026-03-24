# ---------------------------------------------------------
# Program: Linked List Deletion
# Description:
# This program deletes a node with a given value from
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

    def delete_node(self, key):
        current = self.head

        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return

        previous = None
        while current is not None and current.data != key:
            previous = current
            current = current.next

        if current is None:
            print("Value not found in linked list.")
            return

        previous.next = current.next
        current = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print("Original linked list:")
linked_list.display()

linked_list.delete_node(30)

print("Linked list after deleting 30:")
linked_list.display()
