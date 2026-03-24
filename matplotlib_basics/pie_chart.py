# ---------------------------------------------------------
# Program: Pie Chart Example
# Description:
# This program demonstrates a pie chart.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 25, 15, 20]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Language Distribution")
plt.show()
