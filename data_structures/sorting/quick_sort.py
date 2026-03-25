# ---------------------------------------------------------
# Program: Quick Sort
# Description:
# This program sorts an array using quick sort.
# Quick sort selects a pivot and partitions elements
# around the pivot recursively.
# ---------------------------------------------------------

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


numbers = [10, 7, 8, 9, 1, 5]

print("Original array:", numbers)
print("Sorted array:", quick_sort(numbers))
