# ---------------------------------------------------------
# Program: Duplicate Detector
# Description:
# This program checks whether a list contains duplicates
# using a hash map.
# ---------------------------------------------------------

def contains_duplicate(numbers):
    seen = {}

    for number in numbers:
        if number in seen:
            return True
        seen[number] = True

    return False


nums = [10, 20, 30, 40, 20]

print("Numbers:", nums)

if contains_duplicate(nums):
    print("Duplicates found.")
else:
    print("No duplicates found.")
