# ---------------------------------------------------------
# Program: Customize Plot Style
# Description:
# This program demonstrates basic customization of a plot.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 9, 7, 12, 10]

plt.plot(x, y, linestyle='--', marker='o', linewidth=2)
plt.title("Customized Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()
