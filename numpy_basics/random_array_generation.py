# ---------------------------------------------------------
# Program: Random Array Generation
# Description:
# This program demonstrates generating random arrays using NumPy.
# ---------------------------------------------------------

import numpy as np

random_integers = np.random.randint(1, 100, size=(3, 4))
random_decimals = np.random.rand(2, 3)

print("Random Integer Array:")
print(random_integers)

print("\nRandom Decimal Array:")
print(random_decimals)
