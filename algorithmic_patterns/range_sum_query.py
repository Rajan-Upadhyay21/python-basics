# ---------------------------------------------------------
# Program: Range Sum Query
# Description:
# This program builds a prefix sum array and answers
# range sum queries efficiently.
# ---------------------------------------------------------

class RangeSumQuery:
    def __init__(self, numbers):
        self.prefix = [0]

        for number in numbers:
            self.prefix.append(self.prefix[-1] + number)

    def sum_range(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


numbers = [2, 4, 6, 8, 10]
query = RangeSumQuery(numbers)

print("Array:", numbers)
print("Sum from index 1 to 3:", query.sum_range(1, 3))
print("Sum from index 0 to 4:", query.sum_range(0, 4))
