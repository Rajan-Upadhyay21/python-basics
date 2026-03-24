# ---------------------------------------------------------
# Program: Operator Overloading Example
# Description:
# This program demonstrates operator overloading using
# the special __add__ method.
# ---------------------------------------------------------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

result = v1 + v2
print("Result of vector addition:", result)
