# ---------------------------------------------------------
# Program: Generate All Subsets using Recursion
# Description:
# This program generates all possible subsets of a given list
# using recursion. This is also called the power set.
# ---------------------------------------------------------

def generate_subsets(arr, index=0, current_subset=None, all_subsets=None):
    if current_subset is None:
        current_subset = []

    if all_subsets is None:
        all_subsets = []

    # Base case: if index reaches the length of the list
    if index == len(arr):
        all_subsets.append(current_subset.copy())
        return all_subsets

    # Choice 1: exclude current element
    generate_subsets(arr, index + 1, current_subset, all_subsets)

    # Choice 2: include current element
    current_subset.append(arr[index])
    generate_subsets(arr, index + 1, current_subset, all_subsets)

    # Backtrack
    current_subset.pop()

    return all_subsets


# Input list
elements = [1, 2, 3]

print("Original list:")
print(elements)

subsets = generate_subsets(elements)

print("\nAll possible subsets:")
for subset in subsets:
    print(subset)
