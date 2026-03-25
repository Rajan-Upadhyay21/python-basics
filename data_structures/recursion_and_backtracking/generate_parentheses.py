# ---------------------------------------------------------
# Program: Generate Balanced Parentheses
# Description:
# This program generates all valid combinations of n pairs
# of balanced parentheses using backtracking.
# ---------------------------------------------------------

def generate_parentheses(n, open_count, close_count, current, result):
    if len(current) == 2 * n:
        result.append(current)
        return

    if open_count < n:
        generate_parentheses(n, open_count + 1, close_count, current + "(", result)

    if close_count < open_count:
        generate_parentheses(n, open_count, close_count + 1, current + ")", result)


n = 3
result = []

generate_parentheses(n, 0, 0, "", result)

print(f"Balanced parentheses combinations for n = {n}:")
for pattern in result:
    print(pattern)
