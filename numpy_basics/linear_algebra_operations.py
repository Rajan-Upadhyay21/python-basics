# ---------------------------------------------------------
# Program: Linear Algebra Operations
# Description:
# This program demonstrates determinant, inverse,
# and eigenvalues using NumPy.
# ---------------------------------------------------------

import numpy as np

matrix = np.array([
    [4, 2],
    [1, 3]
])

print("Matrix:")
print(matrix)

print("\nDeterminant:")
print(np.linalg.det(matrix))

print("\nInverse:")
print(np.linalg.inv(matrix))

print("\nEigenvalues:")
print(np.linalg.eigvals(matrix))
