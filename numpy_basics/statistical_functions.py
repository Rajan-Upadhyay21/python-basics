# ---------------------------------------------------------
# Program: Statistical Functions
# Description:
# This program demonstrates basic statistical operations in NumPy.
# ---------------------------------------------------------

import numpy as np

data = np.array([12, 18, 25, 30, 45, 50, 65])

print("Data:")
print(data)

print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Sum:", np.sum(data))
