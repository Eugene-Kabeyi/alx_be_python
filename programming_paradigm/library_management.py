# library_management.py

class Book:
    """Represents a single book in the library."""
    
    def __init__(self, title, author):
        self.title = title              # Public attribute
        self.author = author            # Public attribute
        self._is_checked_out = False    # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""
    
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if it’s available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book.title}")
                return
        print(f"Sorry, '{title}' is not available for checkout.")

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Returned: {book.title}")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"No book found with title '{title}'.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
