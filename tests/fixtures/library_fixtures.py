import pytest
from src.user import User
from src.library import Book, LibraryAccount


@pytest.fixture
def sample_user():
    return User("alice", balance=100)


@pytest.fixture
def sample_book():
    return Book("1984", "George Orwell", copies=2)


@pytest.fixture
def single_book():
    def _make(title="Duplicate", author="Author", copies=1):
        return Book(title, author, copies)

    return _make


@pytest.fixture
def multiple_books():
    def _make(*book_specs):
        return [Book(title, author, copies) for title, author, copies in book_specs]

    return _make


@pytest.fixture
def get_book_by_title():
    def _get(account, title):
        return next(b for b in account.borrowed_books if b.title == title)

    return _get


@pytest.fixture
def get_book_by_title_and_author():
    def _get(account, title, author):
        return next(
            b
            for b in account.borrowed_books
            if (b.title == title and b.author == author)
        )

    return _get


@pytest.fixture
def library_users():
    alice = LibraryAccount("Alice")
    borrowed = Book("Python 101", "Guido", copies=1)
    alice.borrow_book(borrowed)

    bob = LibraryAccount("Bob")
    bob.borrowed_books = []

    return [alice, bob]
