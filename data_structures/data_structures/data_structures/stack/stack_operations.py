# ---------------------------------------------------------
# Program: Stack Operations
# Description:
# This program demonstrates push, pop, and display
# operations using a custom stack class.
# ---------------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        print(f"{value} pushed into stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Current stack:", self.items)


stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.display()

print("Popped value:", stack.pop())
stack.display()
