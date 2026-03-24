# ---------------------------------------------------------
# Program: Detect Cycle in Linked List
# Description:
# This program detects whether a linked list contains a cycle
# using slow and fast pointers.
# ---------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Creating linked list with cycle
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

if detect_cycle(node1):
    print("Cycle detected in linked list.")
else:
    print("No cycle detected.")
