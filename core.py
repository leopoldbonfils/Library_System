from .utils import track_access, permission_check


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def __str__(self):
        return f'"{self.title}" by {self.author}'

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, pages={self.pages})"


class Library:
    def __init__(self, name):
        self.name = name
        self._books = []

    def __getitem__(self, index):
        return self._books[index]

    def __len__(self):
        return len(self._books)

    def __repr__(self):
        return f"Library({self.name!r}, {len(self._books)} books)"

    @permission_check("Admin")
    def add_book(self, user, book):
        self._books.append(book)
        print(f"'{book.title}' added by {user.name}.")

    @track_access
    def borrow_book(self, book):
        if book in self._books and not book.is_borrowed:
            book.is_borrowed = True
            print(f"'{book.title}' borrowed successfully.")
        else:
            print(f"'{book.title}' is not available.")

    @track_access
    def return_book(self, book):
        if book in self._books and book.is_borrowed:
            book.is_borrowed = False
            print(f"'{book.title}' returned successfully.")
        else:
            print(f"'{book.title}' was not borrowed from this library.")