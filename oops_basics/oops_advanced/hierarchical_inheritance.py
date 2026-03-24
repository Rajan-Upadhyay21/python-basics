# ---------------------------------------------------------
# Program: Hierarchical Inheritance Example
# Description:
# This program demonstrates one parent class with multiple
# child classes.
# ---------------------------------------------------------

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def car_type(self):
        print("This is a car")


class Bike(Vehicle):
    def bike_type(self):
        print("This is a bike")


car = Car()
bike = Bike()

car.start()
car.car_type()

print()

bike.start()
bike.bike_type()
