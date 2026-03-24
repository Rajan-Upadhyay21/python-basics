# ---------------------------------------------------------
# Program: GroupBy Example
# Description:
# This program demonstrates grouping data and aggregation.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Department": ["AI", "AI", "ML", "ML", "DS"],
    "Employee": ["Rajan", "Amit", "Priya", "Neha", "Arjun"],
    "Salary": [80000, 85000, 90000, 87000, 78000]
}

df = pd.DataFrame(data)

grouped = df.groupby("Department")["Salary"].mean()

print("Average salary by department:")
print(grouped)
