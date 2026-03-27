# ---------------------------------------------------------
# Program: Feature Scaling Example
# Description:
# This program demonstrates standardization of features.
# ---------------------------------------------------------

from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([
    [1, 200],
    [2, 300],
    [3, 400],
    [4, 500]
])

scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)

print("Original data:")
print(X)

print("\nScaled data:")
print(scaled_X)
