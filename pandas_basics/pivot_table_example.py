# ---------------------------------------------------------
# Program: Pivot Table Example
# Description:
# This program demonstrates creating a pivot table in Pandas.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Department": ["AI", "AI", "ML", "ML", "DS"],
    "Employee": ["Rajan", "Amit", "Priya", "Neha", "Arjun"],
    "Salary": [80000, 85000, 90000, 87000, 78000]
}

df = pd.DataFrame(data)

pivot = df.pivot_table(values="Salary", index="Department", aggfunc="mean")

print("Pivot Table:")
print(pivot)
