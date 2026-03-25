# ---------------------------------------------------------
# Program: Generate All Permutations
# Description:
# This program generates all permutations of a list
# using backtracking.
# ---------------------------------------------------------

def generate_permutations(nums, start, result):
    if start == len(nums):
        result.append(nums[:])
        return

    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        generate_permutations(nums, start + 1, result)
        nums[start], nums[i] = nums[i], nums[start]


numbers = [1, 2, 3]
result = []

generate_permutations(numbers, 0, result)

print("All permutations:")
for permutation in result:
    print(permutation)
