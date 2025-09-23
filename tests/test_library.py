import pytest
from src.library import Book

# -------------------------
# Smoke Tests
# -------------------------

@pytest.mark.smoke
class TestLibrarySmoke:


    def test_borrow_book_smoke(self, library_users, sample_book):
        """Smoke test: borrow a new book successfully"""
        account = library_users[1]  # Bob
        account.borrow_book(sample_book)
        assert sample_book in account.borrowed_books


    def test_return_book_smoke(self, library_users, get_book_by_title):
        """Smoke test: return a book successfully"""
        account = library_users[0]  # Alice
        book = get_book_by_title(account, "Python 101")
        account.return_book(book)
        assert book not in account.borrowed_books



# -------------------------
# Regression Tests
# -------------------------

@pytest.mark.regression
class TestLibraryRegression:

    # Borrow book regression tests

    @pytest.mark.parametrize(
        "user_index, book_title, book_author, expect_exception",
        [
            (0, "Python 101", "Guido", True),  # Alice already has this book → fail
            (1, "Learn Pytest", "Author", False),  # Bob can borrow → succeed
            (0, "New Book", "Author", False),  # Alice can borrow a new book → succeed
        ]
    )
    def test_borrow_book_regression(self, library_users, user_index, book_title, book_author, expect_exception, get_book_by_title_and_author):
        account = library_users[user_index]
        if expect_exception:
            with pytest.raises(ValueError):
                book = get_book_by_title_and_author(account, book_title, book_author)
                account.borrow_book(book)
        else:
            book = Book(book_title, book_author)
            books = account.borrow_book(book)
            assert book in books


    # Return book regression tests

    @pytest.mark.parametrize(
        "user_index, book_title, expect_exception",
        [
            (0, "Python 101", False),  # Alice returning a book she borrowed → success
            (1, "Nonexistent Book", True),  # Bob returning a book he didn’t borrow → fail
            (1, "", True),  # Empty string → fail
        ]
    )
    def test_return_book_regression(self, library_users, user_index, book_title, expect_exception, get_book_by_title):
        account = library_users[user_index]
        if expect_exception:
            with pytest.raises(ValueError):
                account.return_book(Book(book_title, "Author"))
        else:
            # find the book object in borrowed_books
            book = get_book_by_title(account, book_title)
            books = account.return_book(book)
            assert book not in books
