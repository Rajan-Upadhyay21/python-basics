# ---------------------------------------------------------
# Program: Stack Using List
# Description:
# This program demonstrates a simple stack implementation
# using a Python list.
# ---------------------------------------------------------

stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)

# Pop element
removed_element = stack.pop()

print("Popped element:", removed_element)
print("Stack after pop:", stack)
