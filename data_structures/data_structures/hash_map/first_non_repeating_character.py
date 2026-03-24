# ---------------------------------------------------------
# Program: First Non-Repeating Character
# Description:
# This program finds the first character in a string
# that does not repeat.
# ---------------------------------------------------------

def first_non_repeating(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] == 1:
            return char

    return None


text = "aabbcddee"

result = first_non_repeating(text)

print("Text:", text)
print("First non-repeating character:", result)
