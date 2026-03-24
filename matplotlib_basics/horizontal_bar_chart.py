# ---------------------------------------------------------
# Program: Horizontal Bar Chart Example
# Description:
# This program demonstrates a horizontal bar chart.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

students = ["Rajan", "Amit", "Priya", "Neha"]
marks = [88, 76, 92, 85]

plt.barh(students, marks)
plt.title("Student Marks")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()
