# ---------------------------------------------------------
# Program: Two Sum Using Hash Map
# Description:
# This program finds two indices such that their values
# add up to a given target.
# ---------------------------------------------------------

def two_sum(numbers, target):
    seen = {}

    for index, value in enumerate(numbers):
        complement = target - value

        if complement in seen:
            return [seen[complement], index]

        seen[value] = index

    return []


nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)

print("Numbers:", nums)
print("Target:", target)
print("Indices:", result)
