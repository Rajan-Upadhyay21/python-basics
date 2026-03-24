# ---------------------------------------------------------
# Program: Find Peak Element
# Description:
# This program finds a peak element using binary search.
# ---------------------------------------------------------

def find_peak_element(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


numbers = [1, 3, 20, 4, 1, 0]

peak_index = find_peak_element(numbers)

print("Array:", numbers)
print("Peak element index:", peak_index)
print("Peak element value:", numbers[peak_index])
