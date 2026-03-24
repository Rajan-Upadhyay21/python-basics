# ---------------------------------------------------------
# Program: Broadcasting Example
# Description:
# This program demonstrates NumPy broadcasting.
# ---------------------------------------------------------

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

result = matrix + vector

print("Matrix:")
print(matrix)

print("\nVector:")
print(vector)

print("\nResult after broadcasting:")
print(result)
