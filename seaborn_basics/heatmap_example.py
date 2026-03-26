# ---------------------------------------------------------
# Program: Seaborn Heatmap
# Description:
# This program demonstrates a basic heatmap using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], columns=["A", "B", "C"])

sns.heatmap(data, annot=True, cmap="YlGnBu")
plt.title("Basic Heatmap")
plt.show()
