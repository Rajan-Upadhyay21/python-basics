# ---------------------------------------------------------
# Program: Constructor Example
# Description:
# This program shows how a constructor initializes object
# data when an object is created.
# ---------------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating object
student1 = Student("Rajan", 23)

# Displaying object data
student1.display()
