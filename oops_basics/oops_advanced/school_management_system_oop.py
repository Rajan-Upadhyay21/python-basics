# ---------------------------------------------------------
# Program: School Management System OOP
# Description:
# This program demonstrates object interaction between
# School, Teacher, and Student classes.
# ---------------------------------------------------------

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def display_school_info(self):
        print("School Name:", self.school_name)

        print("\nTeachers:")
        for teacher in self.teachers:
            print("-", teacher.name, "| Subject:", teacher.subject)

        print("\nStudents:")
        for student in self.students:
            print("-", student.name, "| Grade:", student.grade)


school = School("Chicago Tech Academy")

teacher1 = Teacher("Mr. Smith", "Mathematics")
teacher2 = Teacher("Ms. Johnson", "Computer Science")

student1 = Student("Rajan", "A")
student2 = Student("Amit", "B")

school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.add_student(student1)
school.add_student(student2)

school.display_school_info()
