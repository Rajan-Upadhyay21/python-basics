# ---------------------------------------------------------
# Program: Subplot Example
# Description:
# This program demonstrates multiple plots in one figure.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 10, 8, 12, 18]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y1, marker='o')
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y2)
plt.title("Bar Plot")

plt.tight_layout()
plt.show()
