# ---------------------------------------------------------
# Program: Inheritance Example
# Description:
# This program demonstrates single inheritance in Python.
# ---------------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print("Course:", self.course)


student1 = Student("Rajan", "Computer Science")

student1.show_name()
student1.show_course()
