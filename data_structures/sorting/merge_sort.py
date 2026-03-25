# ---------------------------------------------------------
# Program: Merge Sort
# Description:
# This program sorts an array using merge sort.
# Merge sort follows divide and conquer by splitting
# the array and merging sorted halves.
# ---------------------------------------------------------

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


numbers = [38, 27, 43, 3, 9, 82, 10]

print("Original array:", numbers)
print("Sorted array:", merge_sort(numbers))
