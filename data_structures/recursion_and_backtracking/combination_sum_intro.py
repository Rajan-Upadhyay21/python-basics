# ---------------------------------------------------------
# Program: Combination Sum
# Description:
# This program finds all combinations of numbers
# that add up to a target using backtracking.
# ---------------------------------------------------------

def combination_sum(candidates, target, start, current, result):
    if target == 0:
        result.append(current[:])
        return

    if target < 0:
        return

    for i in range(start, len(candidates)):
        current.append(candidates[i])
        combination_sum(candidates, target - candidates[i], i, current, result)
        current.pop()


candidates = [2, 3, 6, 7]
target = 7
result = []

combination_sum(candidates, target, 0, [], result)

print("Combinations that sum to target:")
for combination in result:
    print(combination)
