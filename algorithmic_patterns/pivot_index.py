# ---------------------------------------------------------
# Program: Pivot Index
# Description:
# This program finds the pivot index where the sum of the
# left side equals the sum of the right side.
# ---------------------------------------------------------

def pivot_index(numbers):
    total_sum = sum(numbers)
    left_sum = 0

    for index, value in enumerate(numbers):
        right_sum = total_sum - left_sum - value

        if left_sum == right_sum:
            return index

        left_sum += value

    return -1


numbers = [1, 7, 3, 6, 5, 6]

print("Array:", numbers)
print("Pivot index:", pivot_index(numbers))
