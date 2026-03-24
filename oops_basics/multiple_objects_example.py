# ---------------------------------------------------------
# Program: Multiple Objects Example
# Description:
# This program demonstrates how multiple objects of the
# same class can store different data.
# ---------------------------------------------------------

class MobilePhone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


phone1 = MobilePhone("Apple", "iPhone 15", 999)
phone2 = MobilePhone("Samsung", "Galaxy S24", 899)
phone3 = MobilePhone("Google", "Pixel 8", 799)

phone1.display_info()
print()
phone2.display_info()
print()
phone3.display_info()
