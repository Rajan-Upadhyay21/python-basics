# ---------------------------------------------------------
# Program: Sys Module Demo
# Description:
# This program demonstrates basic usage of the sys module.
# ---------------------------------------------------------

import sys

print("Python version:", sys.version)
print("Platform:", sys.platform)
print("Module search path:")
for path in sys.path:
    print(path)
