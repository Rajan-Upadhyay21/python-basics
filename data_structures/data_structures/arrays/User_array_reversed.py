# Program: Reverse Array
# Description:
# Asks user for 5 numbers, stores them in array,
# then asks if they want to reverse it.

# Step 1 — Ask user for 5 numbers
arr = []
print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

# Step 2 — Print array
print("\nYour array:", arr)

# Step 3 — Ask if they want to reverse
choice = input("\nDo you want to reverse this array? (yes/no): ")

if choice.lower() == "yes":
    reversed_arr = arr[::-1]
    print("Reversed array:", reversed_arr)
else:
    print("Okay! Your original array stays:", arr)
