# ---------------------------------------------------------
# Program: Character Frequency Map
# Description:
# This program counts how many times each character appears
# in a string using a hash map.
# ---------------------------------------------------------

text = "programming"
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print("Character frequency map:")
for char, count in char_count.items():
    print(char, ":", count)
