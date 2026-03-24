# ---------------------------------------------------------
# Program: Import Random Module
# Description:
# This program demonstrates the use of Python's random
# module for random numbers and choices.
# ---------------------------------------------------------

import random

numbers = [10, 20, 30, 40, 50]

print("Random integer between 1 and 100:", random.randint(1, 100))
print("Random choice from list:", random.choice(numbers))
print("Random float between 0 and 1:", random.random())
