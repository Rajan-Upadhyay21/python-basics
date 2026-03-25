# ---------------------------------------------------------
# Program: Subset Sum Intro
# Description:
# This program checks whether a subset exists
# whose sum equals the target.
# ---------------------------------------------------------

def subset_sum(nums, index, target):
    if target == 0:
        return True

    if index == len(nums) or target < 0:
        return False

    include = subset_sum(nums, index + 1, target - nums[index])
    exclude = subset_sum(nums, index + 1, target)

    return include or exclude


numbers = [3, 34, 4, 12, 5, 2]
target = 9

print("Numbers:", numbers)
print("Target:", target)
print("Subset exists:", subset_sum(numbers, 0, target))
