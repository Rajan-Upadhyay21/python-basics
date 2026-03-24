# ---------------------------------------------------------
# Program: Inventory Management System
# Description:
# This program uses advanced OOP design for inventory items.
# ---------------------------------------------------------

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def restock(self, amount):
        self.quantity += amount

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"{amount} units sold.")
        else:
            print("Not enough stock available.")

    def total_value(self):
        return self.quantity * self.price

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Value:", self.total_value())


item = Product(101, "Keyboard", 50, 25)
item.display()
print()
item.sell(10)
item.display()
