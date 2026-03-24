# ---------------------------------------------------------
# Program: Annotated Plot Example
# Description:
# This program demonstrates adding annotations to a plot.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 20, 30]

plt.plot(x, y, marker='o')
plt.title("Annotated Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.annotate("Highest Point", xy=(5, 30), xytext=(3.5, 28),
             arrowprops=dict(arrowstyle="->"))

plt.show()
