# ---------------------------------------------------------
# Program: Meeting Rooms Check
# Description:
# This program checks whether a person can attend all meetings
# without overlap.
# ---------------------------------------------------------

def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda interval: interval[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


meetings = [[0, 30], [35, 40], [50, 60]]

print("Meetings:", meetings)
print("Can attend all meetings:", can_attend_all_meetings(meetings))
