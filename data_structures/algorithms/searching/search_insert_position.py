# ---------------------------------------------------------
# Program: Search Insert Position
# Description:
# This program returns the index if the target is found.
# Otherwise, it returns the position where it should be inserted.
# ---------------------------------------------------------

def search_insert(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


numbers = [1, 3, 5, 6]
target = 2

print("Array:", numbers)
print("Target:", target)
print("Insert/Search position:", search_insert(numbers, target))
