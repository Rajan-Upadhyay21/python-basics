# ---------------------------------------------------------
# Program: Class Variable Example
# Description:
# This program demonstrates the use of class variables.
# ---------------------------------------------------------

class Employee:
    company_name = "OpenAI"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee Name:", self.name)
        print("Company Name:", Employee.company_name)


employee1 = Employee("Rajan")
employee2 = Employee("Amit")

employee1.display()
print()
employee2.display()
