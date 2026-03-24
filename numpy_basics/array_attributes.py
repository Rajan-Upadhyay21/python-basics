# ---------------------------------------------------------
# Program: Array Attributes
# Description:
# This program demonstrates useful NumPy array attributes.
# ---------------------------------------------------------

import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
print(numbers)

print("\nShape of array:", numbers.shape)
print("Number of dimensions:", numbers.ndim)
print("Data type:", numbers.dtype)
print("Size of array:", numbers.size)
print("Item size in bytes:", numbers.itemsize)
