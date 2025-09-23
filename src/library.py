class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        self.copies = copies

    def is_available(self):
        return self.copies > 0


class LibraryAccount:
    def __init__(self, username):
        self.username = username
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if not book.is_available():
            raise ValueError("Book not available")
        self.borrowed_books.append(book)
        book.copies -= 1
        return self.borrowed_books

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise ValueError("This book was not borrowed")
        self.borrowed_books.remove(book)
        book.copies += 1
        return self.borrowed_books