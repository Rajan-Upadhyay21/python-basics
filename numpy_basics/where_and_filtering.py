# ---------------------------------------------------------
# Program: np.where and Conditional Filtering
# Description:
# This program demonstrates conditional selection in NumPy.
# ---------------------------------------------------------

import numpy as np

numbers = np.array([2, 5, 8, 11, 14, 17, 20])

result = np.where(numbers % 2 == 0, "Even", "Odd")

print("Original Numbers:")
print(numbers)

print("\nClassification:")
print(result)
