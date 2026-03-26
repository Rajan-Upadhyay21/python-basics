# ---------------------------------------------------------
# Program: Seaborn Histogram
# Description:
# This program demonstrates a histogram using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Marks": [55, 60, 65, 70, 75, 80, 85, 90, 95, 88, 76]
})

sns.histplot(data=data, x="Marks", bins=5, kde=True)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
