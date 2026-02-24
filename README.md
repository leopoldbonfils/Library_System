# Smart Library System

A Python package that simulates a library management system using advanced Python concepts: OOP, Dunder Methods, Decorators, Closures, and proper Package structure.

## How to Run

```bash
python -m library_system
```

## Project Structure

```
library_system/
├── __init__.py
├── core.py
├── utils.py
└── __main__.py
```

## Features

**`core.py`** holds the two main classes. `Book` implements `__str__` for readable output, `__len__` to return page count, and `__eq__` to compare books by title and author. `Library` implements `__getitem__` so you can loop over it directly with a `for` loop, plus `add_book` locked behind role-based access and `borrow_book` / `return_book` with automatic logging.

**`utils.py`** holds two things. The `track_access` decorator wraps any method and prints its name, arguments, and a timestamp every time it gets called. The `permission_check` closure takes a required role as an argument and returns a decorator — that decorator checks the user's role before allowing the method to execute, and blocks it with a clear message if the role doesn't match.

**`__main__.py`** is the entry point. It wires everything together and demonstrates all features: access control, iteration, dunder methods, logging, and duck typing.

## MRO Analysis — DigitalBook(Book, Software)

If we were to create a `DigitalBook` class that inherits from both `Book` and a hypothetical `Software` class, Python would resolve method lookup using the **C3 Linearization** algorithm.

```python
class Book:
    pass

class Software:
    pass

class DigitalBook(Book, Software):
    pass
```

Python computes the MRO like this:

```
L[object]      = [object]
L[Book]        = [Book, object]
L[Software]    = [Software, object]

L[DigitalBook] = [DigitalBook]
               + merge([Book, object], [Software, object], [Book, Software])
```

**Step 1:** `Book` is the head of the first list and does not appear in the tail of any other list → take it.

**Step 2:** `object` is now the head of the first list, but it appears in the tail of `[Software, object]` → skip. Move to the next list. `Software` is safe → take it.

**Step 3:** Only `object` remains → take it.

**Final MRO:**

```
DigitalBook → Book → Software → object
```

You can verify this in Python:

```python
print(DigitalBook.__mro__)
# (<class 'DigitalBook'>, <class 'Book'>, <class 'Software'>, <class 'object'>)
```

This guarantees that Python always searches in a consistent, predictable order and avoids the Diamond Problem that breaks naive multiple inheritance in other languages.

## Duck Typing

The `borrow_item` function does not check the type of the object passed to it. It only cares that the object has a `.title` attribute. This means it works on a `Book`, a `Magazine`, or anything else — as long as `.title` exists, it runs.

```python
def borrow_item(item):
    print(f"Borrowing: '{item.title}'")
```

This is the core idea behind duck typing: *if it walks like a duck and quacks like a duck, it's a duck.*
