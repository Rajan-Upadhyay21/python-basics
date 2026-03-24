# ---------------------------------------------------------
# Program: Add and Drop Columns
# Description:
# This program demonstrates adding and removing columns.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Priya"],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)

df["Grade"] = ["B", "C", "A"]

print("After adding Grade column:")
print(df)

df = df.drop("Grade", axis=1)

print("\nAfter dropping Grade column:")
print(df)
