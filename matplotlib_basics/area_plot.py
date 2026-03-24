# ---------------------------------------------------------
# Program: Area Plot Example
# Description:
# This program demonstrates filling the area under a line plot.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 5, 9, 6]

plt.plot(x, y, marker='o')
plt.fill_between(x, y, alpha=0.3)

plt.title("Area Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
