# ---------------------------------------------------------
# Program: Select Columns and Rows
# Description:
# This program demonstrates selecting specific columns
# and rows from a DataFrame.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Priya", "Neha"],
    "Age": [23, 22, 21, 24],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nSelecting 'Name' column:")
print(df["Name"])

print("\nSelecting first two rows:")
print(df.head(2))
