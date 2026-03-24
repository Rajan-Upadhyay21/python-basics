# ---------------------------------------------------------
# Program: Callable Objects Example
# Description:
# This program demonstrates the __call__ method so an object
# can behave like a function.
# ---------------------------------------------------------

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print("Double of 10:", double(10))
print("Triple of 10:", triple(10))
