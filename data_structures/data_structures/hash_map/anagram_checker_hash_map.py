# ---------------------------------------------------------
# Program: Anagram Checker Using Hash Map
# Description:
# This program checks whether two strings are anagrams
# using frequency maps.
# ---------------------------------------------------------

def are_anagrams(text1, text2):
    if len(text1) != len(text2):
        return False

    count = {}

    for char in text1:
        count[char] = count.get(char, 0) + 1

    for char in text2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


word1 = "listen"
word2 = "silent"

print("Word 1:", word1)
print("Word 2:", word2)

if are_anagrams(word1, word2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
