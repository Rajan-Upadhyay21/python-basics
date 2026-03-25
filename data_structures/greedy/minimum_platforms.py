# ---------------------------------------------------------
# Program: Minimum Platforms
# Description:
# This program finds the minimum number of railway platforms
# required so that no train waits.
# ---------------------------------------------------------

def minimum_platforms(arrival, departure):
    arrival.sort()
    departure.sort()

    platform_needed = 1
    max_platforms = 1
    i = 1
    j = 0

    while i < len(arrival) and j < len(departure):
        if arrival[i] <= departure[j]:
            platform_needed += 1
            i += 1
        else:
            platform_needed -= 1
            j += 1

        max_platforms = max(max_platforms, platform_needed)

    return max_platforms


arrival_times = [900, 940, 950, 1100, 1500, 1800]
departure_times = [910, 1200, 1120, 1130, 1900, 2000]

print("Minimum number of platforms needed:", minimum_platforms(arrival_times, departure_times))
