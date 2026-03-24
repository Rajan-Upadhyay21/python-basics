# ---------------------------------------------------------
# Program: Multiple Line Plot Example
# Description:
# This program demonstrates plotting multiple lines in one graph.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales_2024 = [200, 250, 300, 280, 350]
sales_2025 = [220, 270, 320, 300, 370]

plt.plot(months, sales_2024, marker='o', label="2024 Sales")
plt.plot(months, sales_2025, marker='s', label="2025 Sales")

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()
