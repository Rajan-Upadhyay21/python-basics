# ---------------------------------------------------------
# Program: Multiple Inheritance Example
# Description:
# This program demonstrates how a class can inherit from
# more than one parent class.
# ---------------------------------------------------------

class Father:
    def skills_from_father(self):
        print("Father: Gardening and Driving")


class Mother:
    def skills_from_mother(self):
        print("Mother: Cooking and Painting")


class Child(Father, Mother):
    def own_skills(self):
        print("Child: Programming and Communication")


child = Child()
child.skills_from_father()
child.skills_from_mother()
child.own_skills()
