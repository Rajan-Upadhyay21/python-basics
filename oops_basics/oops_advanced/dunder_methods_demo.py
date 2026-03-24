# ---------------------------------------------------------
# Program: Dunder Methods Demo
# Description:
# This program demonstrates special methods like __str__
# and __len__ in a custom class.
# ---------------------------------------------------------

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book Title: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages


book = Book("Python Mastery", 350)
print(book)
print("Length of book object:", len(book))
