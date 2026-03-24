# ---------------------------------------------------------
# Program: Singly Linked List Creation
# Description:
# This program demonstrates how to create a singly linked
# list manually and display its elements.
# ---------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes
node1.next = node2
node2.next = node3

# Head of linked list
head = node1

# Displaying the linked list
current = head
print("Singly Linked List:")
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
