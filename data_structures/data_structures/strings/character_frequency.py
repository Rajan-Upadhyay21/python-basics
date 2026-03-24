# ---------------------------------------------------------
# Program: Character Frequency
# Description:
# This program counts frequency of each character in a string.
# ---------------------------------------------------------

text = "programming"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:")
for char, count in frequency.items():
    print(char, ":", count)
