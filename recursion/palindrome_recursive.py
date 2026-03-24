# ---------------------------------------------------------
# Program: Palindrome Check using Recursion
# Description:
# This program checks whether a given string is a palindrome
# using recursion.
#
# A palindrome reads the same forward and backward.
# Example: "madam", "level"
# ---------------------------------------------------------

def is_palindrome(text):
    # Base case:
    # If the string has 0 or 1 character, it is a palindrome
    if len(text) <= 1:
        return True

    # If first and last characters do not match
    if text[0] != text[-1]:
        return False

    # Recursive case:
    # Check the substring without first and last character
    return is_palindrome(text[1:-1])


# Given word
word = "madam"

# Converting to lowercase for safer comparison
word = word.lower()

# Checking palindrome
if is_palindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
