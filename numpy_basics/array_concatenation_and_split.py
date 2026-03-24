# ---------------------------------------------------------
# Program: Array Concatenation and Splitting
# Description:
# This program demonstrates combining and splitting arrays.
# ---------------------------------------------------------

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

combined = np.concatenate((arr1, arr2))
split_arrays = np.array_split(combined, 3)

print("Combined Array:")
print(combined)

print("\nSplit Arrays:")
for part in split_arrays:
    print(part)
