# ---------------------------------------------------------
# Program: Recursive Binary Search
# Description:
# This program searches for a target element in a sorted
# array using recursive binary search.
# ---------------------------------------------------------

def recursive_binary_search(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, right, target)
    else:
        return recursive_binary_search(arr, left, mid - 1, target)


numbers = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10

result = recursive_binary_search(numbers, 0, len(numbers) - 1, target)

print("Sorted array:", numbers)
print("Target:", target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")
