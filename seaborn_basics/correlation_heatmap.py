# ---------------------------------------------------------
# Program: Correlation Heatmap
# Description:
# This program demonstrates a correlation heatmap using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Math": [78, 85, 90, 72, 88],
    "Science": [80, 82, 91, 70, 89],
    "English": [75, 79, 87, 73, 85],
    "Computer": [88, 90, 95, 80, 92]
})

correlation_matrix = data.corr()

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
