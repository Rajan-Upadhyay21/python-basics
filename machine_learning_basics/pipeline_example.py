# ---------------------------------------------------------
# Program: Pipeline Example
# Description:
# This program demonstrates using a preprocessing and model pipeline.
# ---------------------------------------------------------

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", SVC())
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
