# ---------------------------------------------------------
# Program: K-Means Clustering
# Description:
# This program demonstrates clustering using K-Means.
# ---------------------------------------------------------

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X = iris.data

# Train clustering model
model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X)

print("Cluster labels:")
print(model.labels_)
