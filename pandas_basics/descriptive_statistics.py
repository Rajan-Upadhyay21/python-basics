# ---------------------------------------------------------
# Program: Descriptive Statistics
# Description:
# This program demonstrates basic descriptive statistics in Pandas.
# ---------------------------------------------------------

import pandas as pd

data = {
    "Marks": [85, 78, 92, 88, 95, 74, 81]
}

df = pd.DataFrame(data)

print("Descriptive Statistics:")
print(df.describe())
