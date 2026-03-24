# ---------------------------------------------------------
# Program: Concatenate DataFrames
# Description:
# This program demonstrates combining DataFrames vertically.
# ---------------------------------------------------------

import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Rajan", "Amit"],
    "Marks": [88, 76]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Neha"],
    "Marks": [91, 84]
})

combined_df = pd.concat([df1, df2], ignore_index=True)

print("Concatenated DataFrame:")
print(combined_df)
