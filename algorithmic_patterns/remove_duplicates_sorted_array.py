# ---------------------------------------------------------
# Program: Remove Duplicates from Sorted Array
# Description:
# This program removes duplicates in-place using two pointers.
# ---------------------------------------------------------

def remove_duplicates(numbers):
    if not numbers:
        return 0

    insert_index = 1

    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            numbers[insert_index] = numbers[i]
            insert_index += 1

    return insert_index


numbers = [1, 1, 2, 2, 3, 4, 4]

new_length = remove_duplicates(numbers)

print("New length:", new_length)
print("Updated array:", numbers[:new_length])
