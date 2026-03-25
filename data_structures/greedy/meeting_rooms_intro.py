# ---------------------------------------------------------
# Program: Meeting Rooms Scheduling
# Description:
# This program finds the maximum number of meetings
# that can be held in one room.
# ---------------------------------------------------------

def max_meetings(start, end):
    meetings = sorted(zip(start, end), key=lambda x: x[1])

    count = 1
    last_end = meetings[0][1]

    for i in range(1, len(meetings)):
        if meetings[i][0] > last_end:
            count += 1
            last_end = meetings[i][1]

    return count


start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]

print("Maximum number of meetings:", max_meetings(start_times, end_times))
