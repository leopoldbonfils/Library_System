

from datetime import datetime
from .utils import track_access


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    # User friendly print
    def __str__(self):
        return f"{self.title} by {self.author}"

    # Return number of pages
    def __len__(self):
        return self.pages

    # Compare two books
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author


class Library:
    def __init__(self, name):
        self.name = name
        self._books = []

    # Make library iterable
    def __getitem__(self, index):
        return self._books[index]

    def __len__(self):
        return len(self._books)

    def add_book(self, book):
        self._books.append(book)

    @track_access
    def borrow_book(self, book):
        if book in self._books and not book.is_borrowed:
            book.is_borrowed = True
            print(f"{book.title} borrowed successfully.")
        else:
            print("Book not available.")

    @track_access
    def return_book(self, book):
        if book in self._books and book.is_borrowed:
            book.is_borrowed = False
            print(f"{book.title} returned successfully.")
        else:
            print("Book was not borrowed.")