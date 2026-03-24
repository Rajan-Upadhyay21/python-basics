# ---------------------------------------------------------
# Program: Filter Data
# Description:
# This program demonstrates filtering rows based on conditions.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Priya", "Neha"],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)

filtered_df = df[df["Marks"] > 80]

print("Students with marks greater than 80:")
print(filtered_df)
