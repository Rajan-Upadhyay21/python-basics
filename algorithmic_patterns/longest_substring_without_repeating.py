# ---------------------------------------------------------
# Program: Longest Substring Without Repeating Characters
# Description:
# This program finds the length of the longest substring
# without duplicate characters.
# ---------------------------------------------------------

def longest_unique_substring(text):
    seen = {}
    left = 0
    longest = 0

    for right in range(len(text)):
        char = text[right]

        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right
        longest = max(longest, right - left + 1)

    return longest


text = "abcabcbb"

print("Longest unique substring length:", longest_unique_substring(text))
