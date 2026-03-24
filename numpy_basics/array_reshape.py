# ---------------------------------------------------------
# Program: Array Reshaping
# Description:
# This program demonstrates reshaping NumPy arrays.
# ---------------------------------------------------------

import numpy as np

original_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

reshaped_array = original_array.reshape(3, 4)

print("Original Array:")
print(original_array)

print("\nReshaped Array (3x4):")
print(reshaped_array)
