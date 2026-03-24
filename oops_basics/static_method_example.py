# ---------------------------------------------------------
# Program: Static Method Example
# Description:
# This program demonstrates the use of a static method.
# ---------------------------------------------------------

class MathUtility:
    @staticmethod
    def multiply(a, b):
        return a * b


print("Multiplication:", MathUtility.multiply(6, 7))
