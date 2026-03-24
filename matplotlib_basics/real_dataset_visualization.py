# ---------------------------------------------------------
# Program: Real Dataset Visualization
# Description:
# This program demonstrates plotting data from a simple dataset.
# ---------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Revenue": [1200, 1500, 1700, 1600, 2000]
}

df = pd.DataFrame(data)

plt.plot(df["Month"], df["Revenue"], marker='o')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
