# ---------------------------------------------------------
# Program: Boolean Masking
# Description:
# This program demonstrates filtering array values using conditions.
# ---------------------------------------------------------

import numpy as np

numbers = np.array([5, 12, 18, 7, 25, 30, 3, 42])

mask = numbers > 15
filtered_numbers = numbers[mask]

print("Original Array:")
print(numbers)

print("\nBoolean Mask:")
print(mask)

print("\nFiltered Values Greater Than 15:")
print(filtered_numbers)
