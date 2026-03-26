# ---------------------------------------------------------
# Program: Seaborn Box Plot
# Description:
# This program demonstrates a box plot using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Department": ["AI", "AI", "ML", "ML", "DS", "DS"],
    "Salary": [80000, 85000, 90000, 87000, 75000, 78000]
})

sns.boxplot(data=data, x="Department", y="Salary")
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()
