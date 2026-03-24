# ---------------------------------------------------------
# Program: Handle Missing Values
# Description:
# This program demonstrates finding and filling missing values.
# ---------------------------------------------------------

import pandas as pd
import numpy as np

data = {
    "Name": ["Rajan", "Amit", "Priya", "Neha"],
    "Marks": [85, np.nan, 92, 88],
    "Age": [23, 22, np.nan, 24]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull())

filled_df = df.fillna(0)

print("\nDataFrame after filling missing values:")
print(filled_df)
