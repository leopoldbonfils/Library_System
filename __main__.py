
from library_system import Book, Library


def borrow_item(item):

    print(f"Borrowing: {item.title}")


def main():
    library = Library("City Library")

    book1 = Book("Clean Code", "MUGISHA Leopold", 450)
    book2 = Book("Python Basics", "Danny Jospin", 300)

    library.add_book(book1)
    library.add_book(book2)

    print("All Books:")
    for book in library:
        print(book)

    print("\nBorrowing Book:")
    library.borrow_book(book1)

    print("\nReturning Book:")
    library.return_book(book1)

    print("\nDuck Typing Test:")
    borrow_item(book1)


if __name__ == "__main__":
    main()