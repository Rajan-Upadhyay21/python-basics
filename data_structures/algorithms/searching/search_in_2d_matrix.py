# ---------------------------------------------------------
# Program: Search in 2D Matrix
# Description:
# This program searches for a target value in a sorted 2D matrix.
# ---------------------------------------------------------

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // cols][mid % cols]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 16

print("Matrix:")
for row in matrix:
    print(row)

print("Target:", target)

if search_matrix(matrix, target):
    print("Target found in matrix.")
else:
    print("Target not found in matrix.")
