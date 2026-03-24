# ---------------------------------------------------------
# Program: Read CSV File
# Description:
# This program demonstrates how to read a CSV file in Pandas.
# ---------------------------------------------------------

import pandas as pd

file_name = "students.csv"

sample_data = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Rajan", "Amit", "Priya"],
    "Marks": [88, 76, 91]
})

sample_data.to_csv(file_name, index=False)

df = pd.read_csv(file_name)

print("Data read from CSV:")
print(df)
