# Checking voting eligibility with nested if
age = 20
citizen = "yes"

if age >= 18:
    if citizen == "yes":
        print("Eligible to vote")
    else:
        print("Not eligible because not a citizen")
else:
    print("Not eligible because age is below 18")
