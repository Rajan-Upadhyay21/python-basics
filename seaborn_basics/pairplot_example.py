# ---------------------------------------------------------
# Program: Seaborn Pair Plot
# Description:
# This program demonstrates a pair plot using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Math": [78, 85, 90, 72, 88],
    "Science": [80, 82, 91, 70, 89],
    "English": [75, 79, 87, 73, 85]
})

sns.pairplot(data)
plt.show()
