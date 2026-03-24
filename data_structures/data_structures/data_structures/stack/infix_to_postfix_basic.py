# ---------------------------------------------------------
# Program: Infix to Postfix Conversion
# Description:
# This program converts a simple infix expression to postfix
# using a stack.
# ---------------------------------------------------------

def precedence(operator):
    if operator in ('+', '-'):
        return 1
    if operator in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return "".join(output)


expression = "A+B*C"
print("Infix expression:", expression)
print("Postfix expression:", infix_to_postfix(expression))
