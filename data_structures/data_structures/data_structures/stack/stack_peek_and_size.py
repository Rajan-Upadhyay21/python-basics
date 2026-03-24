# ---------------------------------------------------------
# Program: Stack Peek and Size
# Description:
# This program demonstrates peek and size operations in stack.
# ---------------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(100)
stack.push(200)
stack.push(300)

print("Top element:", stack.peek())
print("Stack size:", stack.size())
