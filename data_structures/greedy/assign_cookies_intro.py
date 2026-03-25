# ---------------------------------------------------------
# Program: Assign Cookies
# Description:
# This program assigns cookies to children to maximize
# the number of satisfied children using a greedy method.
# ---------------------------------------------------------

def find_content_children(children, cookies):
    children.sort()
    cookies.sort()

    child = 0
    cookie = 0

    while child < len(children) and cookie < len(cookies):
        if cookies[cookie] >= children[child]:
            child += 1
        cookie += 1

    return child


children = [1, 2, 3]
cookies = [1, 1]

print("Maximum satisfied children:", find_content_children(children, cookies))
