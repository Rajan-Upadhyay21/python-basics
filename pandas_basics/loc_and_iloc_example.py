# ---------------------------------------------------------
# Program: loc and iloc Example
# Description:
# This program demonstrates label-based and position-based
# indexing in Pandas.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Priya", "Neha"],
    "Marks": [85, 78, 92, 88],
    "Course": ["CS", "DS", "AI", "ML"]
}

df = pd.DataFrame(data)

print("Using loc:")
print(df.loc[0:2, ["Name", "Marks"]])

print("\nUsing iloc:")
print(df.iloc[0:3, 0:2])
