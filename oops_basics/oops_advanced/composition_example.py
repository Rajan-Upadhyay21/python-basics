# ---------------------------------------------------------
# Program: Composition Example
# Description:
# This program demonstrates composition where one class
# contains an object of another class.
# ---------------------------------------------------------

class Engine:
    def start_engine(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        print("Starting car...")
        self.engine.start_engine()


car = Car()
car.start_car()
