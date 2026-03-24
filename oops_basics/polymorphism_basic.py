# ---------------------------------------------------------
# Program: Polymorphism Basic Example
# Description:
# This program demonstrates polymorphism by using the same
# method name in different classes.
# ---------------------------------------------------------

class Dog:
    def sound(self):
        print("Dog barks.")

class Cat:
    def sound(self):
        print("Cat meows.")

class Cow:
    def sound(self):
        print("Cow moos.")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)
make_sound(cat)
make_sound(cow)
