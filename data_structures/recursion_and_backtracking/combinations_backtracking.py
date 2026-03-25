# ---------------------------------------------------------
# Program: Generate Combinations
# Description:
# This program generates all combinations of choosing k elements
# from a list using backtracking.
# ---------------------------------------------------------

def generate_combinations(nums, k, start, current, result):
    if len(current) == k:
        result.append(current[:])
        return

    for i in range(start, len(nums)):
        current.append(nums[i])
        generate_combinations(nums, k, i + 1, current, result)
        current.pop()


numbers = [1, 2, 3, 4]
k = 2
result = []

generate_combinations(numbers, k, 0, [], result)

print(f"All combinations of size {k}:")
for combination in result:
    print(combination)
