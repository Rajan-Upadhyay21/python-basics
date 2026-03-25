# ---------------------------------------------------------
# Program: Letter Combinations of a Phone Number
# Description:
# This program generates all possible letter combinations
# from a digit string using backtracking.
# ---------------------------------------------------------

def backtrack(index, digits, mapping, current, result):
    if index == len(digits):
        result.append(current)
        return

    for char in mapping[digits[index]]:
        backtrack(index + 1, digits, mapping, current + char, result)


digits = "23"
mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

result = []

if digits:
    backtrack(0, digits, mapping, "", result)

print("Letter combinations:")
for combination in result:
    print(combination)
