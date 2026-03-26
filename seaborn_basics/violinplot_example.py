# ---------------------------------------------------------
# Program: Seaborn Violin Plot
# Description:
# This program demonstrates a violin plot using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Category": ["A", "A", "A", "B", "B", "B"],
    "Value": [10, 15, 20, 18, 22, 25]
})

sns.violinplot(data=data, x="Category", y="Value")
plt.title("Violin Plot Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
