# ---------------------------------------------------------
# Program: Activity Selection
# Description:
# This program selects the maximum number of non-overlapping
# activities using a greedy approach.
# ---------------------------------------------------------

def activity_selection(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])

    selected = [activities[0]]
    last_end_time = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            selected.append(activities[i])
            last_end_time = activities[i][1]

    return selected


start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]

selected_activities = activity_selection(start_times, end_times)

print("Selected activities:")
for activity in selected_activities:
    print(activity)
