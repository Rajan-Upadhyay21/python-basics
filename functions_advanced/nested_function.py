# Defining a nested function
def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    inner_function()

# Calling the outer function
outer_function()
