# ---------------------------------------------------------
# Program: Square Root Using Binary Search
# Description:
# This program finds the integer square root of a number
# using binary search.
# ---------------------------------------------------------

def integer_sqrt(number):
    if number < 2:
        return number

    left = 1
    right = number // 2
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == number:
            return mid
        elif square < number:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


number = 27

print("Number:", number)
print("Integer square root:", integer_sqrt(number))
