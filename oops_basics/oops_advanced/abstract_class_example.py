# ---------------------------------------------------------
# Program: Abstract Class Example
# Description:
# This program demonstrates abstraction using Python's
# ABC module and abstract methods.
# ---------------------------------------------------------

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)
print("Area of rectangle:", rectangle.area())
