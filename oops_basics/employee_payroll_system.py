# ---------------------------------------------------------
# Program: Employee Payroll System
# Description:
# This program demonstrates class usage in a payroll-style
# problem by calculating monthly salary and bonus.
# ---------------------------------------------------------

class Employee:
    company_name = "Tech Solutions"

    def __init__(self, employee_id, name, basic_salary):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_bonus(self):
        return self.basic_salary * 0.10

    def calculate_total_salary(self):
        return self.basic_salary + self.calculate_bonus()

    def display_details(self):
        print("Employee ID   :", self.employee_id)
        print("Name          :", self.name)
        print("Company       :", Employee.company_name)
        print("Basic Salary  :", self.basic_salary)
        print("Bonus         :", self.calculate_bonus())
        print("Total Salary  :", self.calculate_total_salary())


employee1 = Employee(201, "Rajan", 6000)
employee1.display_details()
