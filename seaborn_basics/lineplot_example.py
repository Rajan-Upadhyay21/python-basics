# ---------------------------------------------------------
# Program: Seaborn Line Plot
# Description:
# This program demonstrates a basic line plot using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [200, 250, 300, 280, 350]
})

sns.lineplot(data=data, x="Month", y="Sales", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
