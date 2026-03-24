# ---------------------------------------------------------
# Program: Method Overriding Example
# Description:
# This program demonstrates method overriding in inheritance.
# ---------------------------------------------------------

class Animal:
    def sound(self):
        print("Animals make sounds.")


class Dog(Animal):
    def sound(self):
        print("Dog barks.")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()
