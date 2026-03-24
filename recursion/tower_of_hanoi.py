# ---------------------------------------------------------
# Program: Tower of Hanoi using Recursion
# Description:
# This program solves the Tower of Hanoi problem using
# recursion.
#
# Problem:
# Move n disks from source rod to destination rod
# using helper rod, following the rules:
# 1. Only one disk can be moved at a time
# 2. A bigger disk cannot be placed on a smaller disk
# ---------------------------------------------------------

def tower_of_hanoi(n, source, helper, destination):
    # Base case
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Step 1:
    # Move top n-1 disks from source to helper
    tower_of_hanoi(n - 1, source, destination, helper)

    # Step 2:
    # Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Step 3:
    # Move n-1 disks from helper to destination
    tower_of_hanoi(n - 1, helper, source, destination)


# Number of disks
disks = 3

print("Steps to solve Tower of Hanoi:")
tower_of_hanoi(disks, "A", "B", "C")
