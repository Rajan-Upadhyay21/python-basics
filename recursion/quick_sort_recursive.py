# ---------------------------------------------------------
# Program: Quick Sort using Recursion
# Description:
# This program sorts a list using the Quick Sort algorithm.
# Quick Sort is a divide-and-conquer algorithm that:
# 1. Selects a pivot
# 2. Partitions elements into smaller and greater groups
# 3. Recursively sorts both parts
# ---------------------------------------------------------

def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choosing the middle element as pivot
    pivot = arr[len(arr) // 2]

    # Elements smaller than pivot
    left = [x for x in arr if x < pivot]

    # Elements equal to pivot
    middle = [x for x in arr if x == pivot]

    # Elements greater than pivot
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right parts
    return quick_sort(left) + middle + quick_sort(right)


# Example list
numbers = [45, 12, 78, 3, 56, 23, 89, 1, 34, 67, 23]

print("Original list:")
print(numbers)

sorted_numbers = quick_sort(numbers)

print("\nSorted list using Quick Sort:")
print(sorted_numbers)
