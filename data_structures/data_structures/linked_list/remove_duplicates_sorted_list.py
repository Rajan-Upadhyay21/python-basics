# ---------------------------------------------------------
# Program: Remove Duplicates from Sorted Linked List
# Description:
# This program removes duplicate values from a sorted linked list.
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

    def remove_duplicates(self):
        current = self.head

        while current is not None and current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(10)
linked_list.append(20)
linked_list.append(20)
linked_list.append(30)
linked_list.append(30)

print("Original sorted linked list:")
linked_list.display()

linked_list.remove_duplicates()

print("Linked list after removing duplicates:")
linked_list.display()
