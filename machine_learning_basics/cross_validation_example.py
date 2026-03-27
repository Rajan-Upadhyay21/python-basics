# ---------------------------------------------------------
# Program: Cross Validation Example
# Description:
# This program demonstrates cross-validation for model evaluation.
# ---------------------------------------------------------

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

model = LogisticRegression(max_iter=200)
scores = cross_val_score(model, X, y, cv=5)

print("Cross-validation scores:", scores)
print("Average score:", scores.mean())
