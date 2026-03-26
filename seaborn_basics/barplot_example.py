# ---------------------------------------------------------
# Program: Seaborn Bar Plot
# Description:
# This program demonstrates a bar plot using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Department": ["AI", "ML", "DS", "NLP"],
    "Employees": [15, 12, 10, 8]
})

sns.barplot(data=data, x="Department", y="Employees")
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")
plt.show()
