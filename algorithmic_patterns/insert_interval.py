# ---------------------------------------------------------
# Program: Insert Interval
# Description:
# This program inserts a new interval into a list of
# non-overlapping sorted intervals and merges if needed.
# ---------------------------------------------------------

def insert_interval(intervals, new_interval):
    result = []
    i = 0

    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 9]

print("Intervals:", intervals)
print("New interval:", new_interval)
print("Updated intervals:", insert_interval(intervals, new_interval))
