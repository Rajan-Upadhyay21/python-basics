# ---------------------------------------------------------
# Program: Balanced Parentheses
# Description:
# This program checks whether parentheses in an expression
# are balanced using a stack.
# ---------------------------------------------------------

def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


expression = "{[()()]}"
print("Expression:", expression)

if is_balanced(expression):
    print("Balanced parentheses.")
else:
    print("Not balanced.")
