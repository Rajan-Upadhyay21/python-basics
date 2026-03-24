# ---------------------------------------------------------
# Program: Compare Two Files
# Description:
# This program compares the content of two files and checks
# whether they are identical or different.
# ---------------------------------------------------------

file1 = "compare1.txt"
file2 = "compare2.txt"

try:
    # Create sample files
    with open(file1, "w") as f1:
        f1.write("Python programming is fun.\n")
        f1.write("Machine learning is powerful.\n")

    with open(file2, "w") as f2:
        f2.write("Python programming is fun.\n")
        f2.write("Machine learning is powerful.\n")

    # Read both files
    with open(file1, "r") as f1:
        content1 = f1.read()

    with open(file2, "r") as f2:
        content2 = f2.read()

    # Compare contents
    if content1 == content2:
        print("Both files are identical.")
    else:
        print("The files are different.")

except Exception as error:
    print("Unexpected error:", error)
