# ---------------------------------------------------------
# Program: Happy Number
# Description:
# This program checks if a number is happy
# using the fast and slow pointers idea.
# ---------------------------------------------------------

def next_number(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


def is_happy(n):
    slow = n
    fast = n

    while True:
        slow = next_number(slow)
        fast = next_number(next_number(fast))

        if fast == 1:
            return True

        if slow == fast:
            return False


number = 19

print("Is happy number:", is_happy(number))
