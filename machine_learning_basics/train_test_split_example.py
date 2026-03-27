# ---------------------------------------------------------
# Program: Train-Test Split Example
# Description:
# This program demonstrates how to split a dataset into
# training and testing sets.
# ---------------------------------------------------------

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load sample dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Total samples:", len(X))
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
