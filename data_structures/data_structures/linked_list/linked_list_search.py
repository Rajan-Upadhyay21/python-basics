# ---------------------------------------------------------
# Program: Linked List Search
# Description:
# This program searches for a value in a linked list.
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

    def search(self, key):
        position = 0
        current = self.head

        while current is not None:
            if current.data == key:
                return position
            current = current.next
            position += 1

        return -1

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.append(11)
linked_list.append(22)
linked_list.append(33)
linked_list.append(44)

linked_list.display()

target = 33
result = linked_list.search(target)

if result != -1:
    print(f"Value {target} found at position {result}.")
else:
    print(f"Value {target} not found.")
