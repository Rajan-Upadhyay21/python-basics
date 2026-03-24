# ---------------------------------------------------------
# Program: Merge Sort using Recursion
# Description:
# This program sorts a list using the recursive merge sort
# algorithm.
#
# Merge sort follows divide and conquer:
# 1. Divide the list into two halves
# 2. Recursively sort each half
# 3. Merge the sorted halves
# ---------------------------------------------------------

def merge_sort(arr):
    # Base case:
    # A list of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # Finding the middle index
    mid = len(arr) // 2

    # Dividing the array into left and right halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sorting both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merging the sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    merged = []
    i = 0
    j = 0

    # Compare elements from both lists and append smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from left list
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add remaining elements from right list
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Original list
numbers = [38, 27, 43, 3, 9, 82, 10]

print("Original list:")
print(numbers)

# Sorting using merge sort
sorted_numbers = merge_sort(numbers)

print("Sorted list:")
print(sorted_numbers)
