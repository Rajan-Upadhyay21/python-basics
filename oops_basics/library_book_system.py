# ---------------------------------------------------------
# Program: Library Book System
# Description:
# This program demonstrates object-oriented programming
# using a simple library and book availability system.
# ---------------------------------------------------------

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def issue_book(self):
        if self.available:
            self.available = False
            print(f"Book '{self.title}' has been issued successfully.")
        else:
            print(f"Book '{self.title}' is currently not available.")

    def return_book(self):
        self.available = True
        print(f"Book '{self.title}' has been returned successfully.")

    def display_book_info(self):
        print("Book ID      :", self.book_id)
        print("Title        :", self.title)
        print("Author       :", self.author)
        print("Available    :", self.available)


book1 = Book(1, "Python Programming", "John Smith")

book1.display_book_info()
print()

book1.issue_book()
book1.display_book_info()
print()

book1.return_book()
book1.display_book_info()
