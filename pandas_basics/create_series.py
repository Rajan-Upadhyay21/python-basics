# ---------------------------------------------------------
# Program: Create Pandas Series
# Description:
# This program demonstrates how to create a Pandas Series.
# ---------------------------------------------------------

import pandas as pd

student_marks = pd.Series([85, 90, 78, 92, 88], index=["A", "B", "C", "D", "E"])

print("Pandas Series:")
print(student_marks)
