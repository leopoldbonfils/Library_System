from .core import Book, Library


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


def borrow_item(item):
    print(f"Borrowing: '{item.title}'")


def main():
    library = Library("City Library")

    admin = User("MUGISHA Leopold", "Admin")
    guest = User("Danny Jospin", "Guest")

    book1 = Book("Clean Code", "Robert C. Martin", 450)
    book2 = Book("Python Basics", "Danny Jospin", 300)
    book3 = Book("The Pragmatic Programmer", "David Thomas", 352)

    print("=== Access Control ===")
    library.add_book(admin, book1)
    library.add_book(admin, book2)
    library.add_book(guest, book3)

    print("\n=== All Books in Library ===")
    for book in library:
        print(book)

    print("\n=== Dunder Methods ===")
    print(f"str  : {book1}")
    print(f"len  : {len(book1)} pages")
    print(f"eq   : book1 == book1 copy? {book1 == Book('Clean Code', 'Robert C. Martin', 999)}")
    print(f"eq   : book1 == book2? {book1 == book2}")

    print("\n=== Borrow & Return (track_access) ===")
    library.borrow_book(book1)
    library.borrow_book(book1)
    library.return_book(book1)
    library.return_book(book2)

    print("\n=== Duck Typing ===")

    class Magazine:
        def __init__(self, title):
            self.title = title

    borrow_item(book1)
    borrow_item(Magazine("Nature Weekly"))


if __name__ == "__main__":
    main()