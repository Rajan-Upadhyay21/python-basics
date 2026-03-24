# ---------------------------------------------------------
# Program: Bar Chart Example
# Description:
# This program demonstrates a vertical bar chart.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

categories = ["Python", "Java", "C++", "JavaScript"]
values = [90, 75, 65, 80]

plt.bar(categories, values)
plt.title("Programming Language Popularity")
plt.xlabel("Languages")
plt.ylabel("Popularity Score")
plt.show()
