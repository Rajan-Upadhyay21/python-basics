# ---------------------------------------------------------
# Program: Line Plot Example
# Description:
# This program demonstrates a basic line plot using Matplotlib.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o')
plt.title("Basic Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
