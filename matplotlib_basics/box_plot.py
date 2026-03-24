# ---------------------------------------------------------
# Program: Box Plot Example
# Description:
# This program demonstrates a box plot.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

data = [12, 15, 14, 18, 21, 19, 13, 16, 20, 22, 30]

plt.boxplot(data)
plt.title("Box Plot Example")
plt.ylabel("Values")
plt.show()
