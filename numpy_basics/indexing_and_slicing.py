# ---------------------------------------------------------
# Program: Indexing and Slicing
# Description:
# This program demonstrates how to access elements and slices
# in a NumPy array.
# ---------------------------------------------------------

import numpy as np

arr = np.array([5, 10, 15, 20, 25, 30, 35])

print("Original Array:")
print(arr)

print("\nElement at index 2:", arr[2])
print("Last element:", arr[-1])
print("Slice from index 1 to 4:", arr[1:5])
print("Every second element:", arr[::2])
