# ---------------------------------------------------------
# Program: Generate All Permutations using Recursion
# Description:
# This program generates all possible permutations of a list
# using recursion and backtracking.
# ---------------------------------------------------------

def generate_permutations(arr, start=0):
    # Base case: if start reaches end, one permutation is complete
    if start == len(arr):
        print(arr[:])
        return

    # Try placing each element at current position
    for i in range(start, len(arr)):
        # Swap current element with start
        arr[start], arr[i] = arr[i], arr[start]

        # Recursive call for next position
        generate_permutations(arr, start + 1)

        # Backtrack to restore original order
        arr[start], arr[i] = arr[i], arr[start]


# Input list
elements = [1, 2, 3]

print("Original list:")
print(elements)
print("\nAll permutations:")

generate_permutations(elements)
