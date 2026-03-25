# ---------------------------------------------------------
# Program: Custom Object Sorting
# Description:
# This program sorts custom objects using a key function.
# ---------------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"Student(name='{self.name}', marks={self.marks})"


students = [
    Student("Rajan", 88),
    Student("Amit", 76),
    Student("Priya", 92),
    Student("Neha", 84)
]

sorted_students = sorted(students, key=lambda student: student.marks)

print("Students sorted by marks:")
for student in sorted_students:
    print(student)
