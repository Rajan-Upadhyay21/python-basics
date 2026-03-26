# ---------------------------------------------------------
# Program: Seaborn Count Plot
# Description:
# This program demonstrates a count plot using Seaborn.
# ---------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Course": ["AI", "ML", "AI", "DS", "ML", "AI", "NLP"]
})

sns.countplot(data=data, x="Course")
plt.title("Course Frequency")
plt.xlabel("Course")
plt.ylabel("Count")
plt.show()
