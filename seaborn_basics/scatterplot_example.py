# ---------------------------------------------------------
# Program: Seaborn Scatter Plot
# Description:
# This program demonstrates a scatter plot using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7],
    "Marks": [45, 50, 55, 65, 70, 80, 90]
})

sns.scatterplot(data=data, x="Hours_Studied", y="Marks")
plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()
