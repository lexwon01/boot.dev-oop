class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        keep = []
        for b in self.books:
            if b.title != book.title or b.author != book.author:
                keep.append(b)
            self.books = keep

    def search_books(self, search_string):
        results = []
        search_lower = search_string.lower()
        for book in self.books:
            if search_lower in book.title.lower() or search_lower in book.author.lower():
                results.append(book)
        return results
