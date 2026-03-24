# ---------------------------------------------------------
# Program: Getter and Setter Example
# Description:
# This program demonstrates how getter and setter methods
# are used to access and modify private data safely.
# ---------------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks. Enter value between 0 and 100.")

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)


student1 = Student("Rajan", 85)

student1.display()
print("Current Marks:", student1.get_marks())

student1.set_marks(92)
student1.display()
