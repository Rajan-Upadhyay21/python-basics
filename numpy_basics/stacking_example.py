# ---------------------------------------------------------
# Program: Stacking Arrays
# Description:
# This program demonstrates vertical and horizontal stacking.
# ---------------------------------------------------------

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

vertical_stack = np.vstack((arr1, arr2))
horizontal_stack = np.hstack((arr1, arr2))

print("Vertical Stack:")
print(vertical_stack)

print("\nHorizontal Stack:")
print(horizontal_stack)
