# ---------------------------------------------------------
# Program: Property Decorator Example
# Description:
# This program demonstrates @property and setter methods.
# ---------------------------------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

    def display(self):
        print("Product:", self.name)
        print("Price:", self._price)


product = Product("Laptop", 1200)
product.display()
product.price = 1500
product.display()
