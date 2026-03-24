# ---------------------------------------------------------
# Program: Aggregation Example
# Description:
# This program demonstrates aggregation where one object
# uses another object without owning its lifecycle fully.
# ---------------------------------------------------------

class Department:
    def __init__(self, department_name):
        self.department_name = department_name


class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_info(self):
        print("Employee Name:", self.name)
        print("Department:", self.department.department_name)


dept = Department("AI Research")
employee = Employee("Rajan", dept)

employee.display_info()
