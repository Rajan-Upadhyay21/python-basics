# ---------------------------------------------------------
# Program: PCA Dimensionality Reduction
# Description:
# This program demonstrates dimensionality reduction using PCA.
# ---------------------------------------------------------

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)
print("Reduced data:")
print(X_reduced[:5])
