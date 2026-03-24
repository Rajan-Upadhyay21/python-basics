# ---------------------------------------------------------
# Program: Save Figure Example
# Description:
# This program demonstrates saving a chart as an image file.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title("Plot Saved as Image")
plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("saved_plot.png")
plt.show()
