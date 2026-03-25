# ---------------------------------------------------------
# Program: Gas Station
# Description:
# This program finds the starting gas station index
# from which the full circuit can be completed.
# ---------------------------------------------------------

def can_complete_circuit(gas, cost):
    total_tank = 0
    current_tank = 0
    start_index = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]

        if current_tank < 0:
            start_index = i + 1
            current_tank = 0

    return start_index if total_tank >= 0 else -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print("Starting gas station index:", can_complete_circuit(gas, cost))
