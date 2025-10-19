class Book:
    def __init__(self, title, author, year):
        """Constructor that initializes the book details."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor called when the object is deleted."""
        print(f"Deleting {self.title}")

