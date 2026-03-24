# ---------------------------------------------------------
# Program: Interpolation Search
# Description:
# This program searches for a target element in a uniformly
# distributed sorted array using interpolation search.
# ---------------------------------------------------------

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and low < len(arr) and high < len(arr) and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        position = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[position] == target:
            return position

        if arr[position] < target:
            low = position + 1
        else:
            high = position - 1

    return -1


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70

result = interpolation_search(numbers, target)

print("Sorted array:", numbers)
print("Target:", target)
print("Result index:", result)
