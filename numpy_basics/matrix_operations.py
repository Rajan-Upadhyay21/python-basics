# ---------------------------------------------------------
# Program: Matrix Operations
# Description:
# This program demonstrates matrix addition, transpose,
# and matrix multiplication.
# ---------------------------------------------------------

import numpy as np

matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nMatrix Addition:")
print(matrix_a + matrix_b)

print("\nTranspose of Matrix A:")
print(matrix_a.T)

print("\nMatrix Multiplication:")
print(np.dot(matrix_a, matrix_b))
