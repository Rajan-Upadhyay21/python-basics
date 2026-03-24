# ---------------------------------------------------------
# Program: super() Keyword Example
# Description:
# This program demonstrates the use of super() to call
# parent class constructor and methods.
# ---------------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display_employee(self):
        self.display_name()
        print("Employee ID:", self.employee_id)


employee = Employee("Rajan", 101)
employee.display_employee()
