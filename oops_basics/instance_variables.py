# ---------------------------------------------------------
# Program: Instance Variables Example
# Description:
# This program demonstrates the use of instance variables
# inside a class.
# ---------------------------------------------------------

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

car1.display_info()
print()
car2.display_info()
