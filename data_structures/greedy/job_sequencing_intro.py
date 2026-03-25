# ---------------------------------------------------------
# Program: Job Sequencing
# Description:
# This program schedules jobs to maximize profit
# before their deadlines using a greedy approach.
# ---------------------------------------------------------

def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs:
        for slot in range(deadline - 1, -1, -1):
            if slots[slot] == -1:
                slots[slot] = job_id
                total_profit += profit
                break

    scheduled_jobs = [job for job in slots if job != -1]
    return scheduled_jobs, total_profit


jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

scheduled_jobs, profit = job_sequencing(jobs)

print("Scheduled jobs:", scheduled_jobs)
print("Total profit:", profit)
