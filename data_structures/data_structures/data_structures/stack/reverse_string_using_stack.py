# ---------------------------------------------------------
# Program: Reverse String Using Stack
# Description:
# This program reverses a string using stack logic.
# ---------------------------------------------------------

def reverse_string(text):
    stack = []

    for char in text:
        stack.append(char)

    reversed_text = ""
    while stack:
        reversed_text += stack.pop()

    return reversed_text


text = "Python"
print("Original string:", text)
print("Reversed string:", reverse_string(text))
