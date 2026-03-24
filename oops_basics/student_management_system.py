# ---------------------------------------------------------
# Program: Student Management System
# Description:
# This program uses a class to store and display student
# information in a simple management-style format.
# ---------------------------------------------------------

class Student:
    def __init__(self, student_id, name, course, marks):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks

    def display_student(self):
        print("Student ID   :", self.student_id)
        print("Name         :", self.name)
        print("Course       :", self.course)
        print("Marks        :", self.marks)

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"


student1 = Student(101, "Rajan", "Computer Science", 88)

student1.display_student()
print("Grade        :", student1.calculate_grade())
