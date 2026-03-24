# ---------------------------------------------------------
# Program: Stacked Bar Chart Example
# Description:
# This program demonstrates stacked bar charts.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
boys = [75, 80, 70]
girls = [85, 78, 88]

plt.bar(subjects, boys, label="Boys")
plt.bar(subjects, girls, bottom=boys, label="Girls")

plt.title("Marks Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.show()
