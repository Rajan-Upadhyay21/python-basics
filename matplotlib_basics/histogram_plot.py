# ---------------------------------------------------------
# Program: Histogram Example
# Description:
# This program demonstrates a histogram for numerical data.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

data = [12, 15, 14, 10, 18, 21, 19, 17, 13, 16, 18, 20, 22]

plt.hist(data, bins=5, edgecolor="black")
plt.title("Histogram of Data")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()
