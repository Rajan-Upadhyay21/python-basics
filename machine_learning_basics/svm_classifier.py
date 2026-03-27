# ---------------------------------------------------------
# Program: Support Vector Machine Classifier
# Description:
# This program demonstrates classification using SVM.
# ---------------------------------------------------------

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = SVC(kernel="linear")
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
