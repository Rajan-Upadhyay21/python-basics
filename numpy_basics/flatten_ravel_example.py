# ---------------------------------------------------------
# Program: Flatten and Ravel
# Description:
# This program demonstrates converting multi-dimensional arrays
# into 1D arrays.
# ---------------------------------------------------------

import numpy as np

array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flattened = array_2d.flatten()
raveled = array_2d.ravel()

print("Original Array:")
print(array_2d)

print("\nFlattened Array:")
print(flattened)

print("\nRaveled Array:")
print(raveled)
