# ---------------------------------------------------------
# Program: Method Example
# Description:
# This program demonstrates how methods work inside a class.
# ---------------------------------------------------------

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()

print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
