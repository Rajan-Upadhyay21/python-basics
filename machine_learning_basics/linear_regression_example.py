# ---------------------------------------------------------
# Program: Linear Regression Example
# Description:
# This program demonstrates a basic linear regression model.
# ---------------------------------------------------------

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Sample dataset
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([2, 4, 5, 4, 5, 7])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Actual values:", y_test)
print("Predicted values:", predictions)
print("Mean Squared Error:", mean_squared_error(y_test, predictions))
