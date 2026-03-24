# ---------------------------------------------------------
# Program: Linked List Length
# Description:
# This program calculates the number of nodes in a linked list.
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

    def find_length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.append(100)
linked_list.append(200)
linked_list.append(300)
linked_list.append(400)
linked_list.append(500)

linked_list.display()
print("Length of linked list:", linked_list.find_length())
