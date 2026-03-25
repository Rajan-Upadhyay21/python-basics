# ---------------------------------------------------------
# Program: Generate All Subsets
# Description:
# This program generates all subsets of a list
# using recursion and backtracking.
# ---------------------------------------------------------

def generate_subsets(nums, index, current, result):
    if index == len(nums):
        result.append(current[:])
        return

    # Exclude current element
    generate_subsets(nums, index + 1, current, result)

    # Include current element
    current.append(nums[index])
    generate_subsets(nums, index + 1, current, result)

    # Backtrack
    current.pop()


numbers = [1, 2, 3]
result = []

generate_subsets(numbers, 0, [], result)

print("All subsets:")
for subset in result:
    print(subset)
