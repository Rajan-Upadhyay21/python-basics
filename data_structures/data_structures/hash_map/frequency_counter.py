# ---------------------------------------------------------
# Program: Frequency Counter
# Description:
# This program counts the frequency of each number in a list
# using a hash map.
# ---------------------------------------------------------

numbers = [1, 2, 3, 2, 4, 1, 5, 2, 3, 1, 1]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print("Number frequency:")
for key, value in frequency.items():
    print(key, ":", value)
