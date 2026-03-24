# ---------------------------------------------------------
# Program: Sort Values
# Description:
# This program demonstrates sorting a DataFrame by a column.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Priya", "Neha"],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values(by="Marks", ascending=False)

print("Data sorted by marks in descending order:")
print(sorted_df)
