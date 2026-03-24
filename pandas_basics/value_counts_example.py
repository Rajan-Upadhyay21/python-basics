# ---------------------------------------------------------
# Program: Value Counts Example
# Description:
# This program demonstrates counting unique values in a column.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Department": ["AI", "ML", "AI", "DS", "ML", "AI"]
}

df = pd.DataFrame(data)

print("Value counts for Department:")
print(df["Department"].value_counts())
