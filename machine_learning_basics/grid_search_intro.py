# ---------------------------------------------------------
# Program: Grid Search Intro
# Description:
# This program demonstrates hyperparameter tuning using GridSearchCV.
# ---------------------------------------------------------

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

param_grid = {
    "C": [0.1, 1, 10],
    "kernel": ["linear", "rbf"]
}

grid_search = GridSearchCV(SVC(), param_grid, cv=3)
grid_search.fit(X, y)

print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
