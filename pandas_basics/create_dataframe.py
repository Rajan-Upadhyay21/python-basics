# ---------------------------------------------------------
# Program: Create Pandas DataFrame
# Description:
# This program demonstrates how to create a DataFrame.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Name": ["Rajan", "Amit", "Priya", "Neha"],
    "Age": [23, 22, 21, 24],
    "Course": ["CS", "DS", "AI", "ML"]
}

df = pd.DataFrame(data)

print("Pandas DataFrame:")
print(df)
