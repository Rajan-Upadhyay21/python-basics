# ---------------------------------------------------------
# Program: Jump Game
# Description:
# This program checks whether the last index can be reached
# using a greedy approach.
# ---------------------------------------------------------

def can_jump(nums):
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False

        farthest = max(farthest, i + nums[i])

    return True


numbers = [2, 3, 1, 1, 4]

print("Array:", numbers)
print("Can reach last index:", can_jump(numbers))
