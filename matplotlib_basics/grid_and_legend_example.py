# ---------------------------------------------------------
# Program: Grid and Legend Example
# Description:
# This program demonstrates the use of grid and legend.
# ---------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
team_a = [10, 15, 20, 18, 25]
team_b = [8, 12, 18, 22, 28]

plt.plot(x, team_a, marker='o', label="Team A")
plt.plot(x, team_b, marker='s', label="Team B")

plt.title("Performance Comparison")
plt.xlabel("Round")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.show()
