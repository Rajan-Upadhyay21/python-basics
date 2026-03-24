# ---------------------------------------------------------
# Program: Palindrome Check
# Description:
# This program checks whether a string is palindrome.
# ---------------------------------------------------------

text = "madam"

if text == text[::-1]:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
