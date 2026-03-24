# ---------------------------------------------------------
# Program: Merge DataFrames
# Description:
# This program demonstrates merging two DataFrames.
# ---------------------------------------------------------

import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Rajan", "Amit", "Priya"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [88, 76, 91]
})

merged_df = pd.merge(students, marks, on="ID")

print("Merged DataFrame:")
print(merged_df)
