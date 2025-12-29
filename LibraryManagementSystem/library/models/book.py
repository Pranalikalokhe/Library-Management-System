class Book:
    def __init__(self, isbn, title, author, available=True):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }
