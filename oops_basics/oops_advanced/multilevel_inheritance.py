# ---------------------------------------------------------
# Program: Multilevel Inheritance Example
# Description:
# This program demonstrates inheritance across multiple
# levels of classes.
# ---------------------------------------------------------

class Grandparent:
    def family_origin(self):
        print("Family origin: Gujarat")


class Parent(Grandparent):
    def profession(self):
        print("Profession: Engineer")


class Child(Parent):
    def education(self):
        print("Education: Computer Science")


child = Child()
child.family_origin()
child.profession()
child.education()
