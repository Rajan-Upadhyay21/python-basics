# ---------------------------------------------------------
# Program: Exception Propagation Demo
# Description:
# This program demonstrates how exceptions move from one
# function to another until they are handled.
# ---------------------------------------------------------

def level_three():
    print("Inside level_three()")
    raise ValueError("An error occurred in level three.")

def level_two():
    print("Inside level_two()")
    level_three()

def level_one():
    print("Inside level_one()")
    level_two()


try:
    level_one()

except ValueError as error:
    print("Caught propagated exception:", error)

finally:
    print("Exception propagation demo completed.")
