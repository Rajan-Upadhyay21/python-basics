# ---------------------------------------------------------
# Program: Scatter Plot Example
# Description:
# This program demonstrates a scatter plot.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7]
marks_scored = [45, 50, 55, 65, 70, 80, 90]

plt.scatter(hours_studied, marks_scored)
plt.title("Hours Studied vs Marks Scored")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.show()
