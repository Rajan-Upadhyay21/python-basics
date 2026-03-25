# ---------------------------------------------------------
# Program: Restore IP Addresses
# Description:
# This program generates all valid IP addresses
# from a digit string using backtracking.
# ---------------------------------------------------------

def is_valid(segment):
    if len(segment) > 1 and segment[0] == "0":
        return False
    return 0 <= int(segment) <= 255


def restore_ip_addresses(text, start, parts, current, result):
    if parts == 4 and start == len(text):
        result.append(".".join(current))
        return

    if parts == 4 or start == len(text):
        return

    for end in range(start + 1, min(start + 4, len(text) + 1)):
        segment = text[start:end]

        if is_valid(segment):
            current.append(segment)
            restore_ip_addresses(text, end, parts + 1, current, result)
            current.pop()


text = "25525511135"
result = []

restore_ip_addresses(text, 0, 0, [], result)

print("Valid IP addresses:")
for ip in result:
    print(ip)
