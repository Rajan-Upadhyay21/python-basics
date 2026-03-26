# ---------------------------------------------------------
# Program: First True Condition
# Description:
# This program demonstrates boundary-style binary search
# to find the first True value in a boolean array.
# ---------------------------------------------------------

def first_true(arr):
    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] is True:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


values = [False, False, False, True, True, True]

print("Boolean array:", values)
print("First True index:", first_true(values))
