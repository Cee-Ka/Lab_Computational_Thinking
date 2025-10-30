class Book:
    def __init__(self, title, author):
        self.title, self.author, self.status = title, author, "available"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for b in self.books:
            if b.title == title and b.status == "available":
                b.status = "borrowed"; print(f"Borrow: {b.title}"); return
        print("Cannot borrow.")

    def return_book(self, title):
        for b in self.books:
            if b.title == title and b.status == "borrowed":
                b.status = "available"; print(f"Return: {b.title}"); return
        print("Cannot return.")

    def list_available(self):
        print("Available books:")
        for b in self.books:
            if b.status == "available":
                print(f"- {b.title} ({b.author})")

lib = Library()
lib.add_book(Book("1984", "Orwell"))
lib.add_book(Book("HP", "Rowling"))
lib.borrow_book("1984")
lib.return_book("1984")
lib.list_available()
