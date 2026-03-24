# ---------------------------------------------------------
# Program: Handle Duplicates
# Description:
# This program demonstrates detecting and removing duplicate rows.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Rajan", "Neha"],
    "Marks": [85, 78, 85, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nDuplicate Rows:")
print(df.duplicated())

clean_df = df.drop_duplicates()

print("\nDataFrame after removing duplicates:")
print(clean_df)
