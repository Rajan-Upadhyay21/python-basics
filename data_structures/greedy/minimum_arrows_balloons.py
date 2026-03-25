# ---------------------------------------------------------
# Program: Minimum Number of Arrows to Burst Balloons
# Description:
# This program finds the minimum arrows required to burst
# all balloons using a greedy interval strategy.
# ---------------------------------------------------------

def find_min_arrows(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])
    arrows = 1
    current_end = points[0][1]

    for start, end in points[1:]:
        if start > current_end:
            arrows += 1
            current_end = end

    return arrows


balloons = [[10, 16], [2, 8], [1, 6], [7, 12]]

print("Minimum arrows required:", find_min_arrows(balloons))
