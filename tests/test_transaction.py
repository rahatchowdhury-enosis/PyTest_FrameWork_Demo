import pytest
from src.transactions import Transaction
from src.library import Book


# --------------------------
# Integration library transaction tests
# --------------------------


@pytest.mark.integration
class TestTransactionIntegration:


    @pytest.mark.smoke
    class TestTransactionIntegrationSmoke:

        # --------------------------
        # Existing borrow + fee tests
        # --------------------------

        # critical path: borrow + pay fee
        def test_user_borrow_and_pay_fee(self, sample_user, sample_book):
            sample_user.account.borrow_book(sample_book)
            txn = Transaction(sample_user)
            msg = txn.charge_late_fee(20)
            assert "Late fee" in msg
            assert sample_user.balance == 80


        # --------------------------
        # New add_funds tests
        # --------------------------

        # critical: adding funds works normally
        def test_transaction_add_funds_normal(self, sample_user):
            txn = Transaction(sample_user)
            starting_balance = sample_user.balance
            msg = txn.add_funds(50)
            assert sample_user.balance == starting_balance + 50
            assert f"{50} added to {sample_user.username}" in msg


    @pytest.mark.regression
    class TestTransactionIntegrationRegression:

        # --------------------------
        # Existing borrow + fee tests
        # --------------------------

        # covers multiple books & multiple fees = edge scenario
        def test_multiple_books_and_fees(self, sample_user):
            book1 = Book("Book 1", "Author 1", copies=2)
            book2 = Book("Book 2", "Author 2", copies=1)
            sample_user.account.borrow_book(book1)
            sample_user.account.borrow_book(book2)
            txn = Transaction(sample_user)
            txn.charge_late_fee(10)
            txn.charge_late_fee(15)
            assert sample_user.balance == 75


        # edge case: borrowing same book twice
        def test_edge_case_borrow_same_book(self, sample_user):
            book = Book("Duplicate", "Author", copies=1)
            sample_user.account.borrow_book(book)
            with pytest.raises(ValueError):
                sample_user.account.borrow_book(book)


        # edge case: returning a book never borrowed
        def test_edge_case_return_not_borrowed(self, sample_user):
            book = Book("Not Borrowed", "Author", copies=1)
            with pytest.raises(ValueError):
                sample_user.account.return_book(book)

        # --------------------------
        # New add_funds tests
        # --------------------------


        # multiple additions = edge case
        def test_transaction_add_funds_multiple_times(self, sample_user):
            txn = Transaction(sample_user)
            starting_balance = sample_user.balance
            txn.add_funds(30)
            txn.add_funds(20)
            assert sample_user.balance == starting_balance + 50


        # negative scenario: invalid amount
        def test_transaction_add_funds_negative_amount(self, sample_user):
            txn = Transaction(sample_user)
            with pytest.raises(ValueError):
                txn.add_funds(-10)


# --------------------------
# Standalone library transaction tests
# --------------------------

@pytest.mark.standAlone
class TestTransactionStandAlone:

    @pytest.mark.smoke
    class TestTransactionStandAloneSmoke:

        # critical path: borrow a book successfully
        def test_user_borrow_book(self, sample_user, sample_book):
            sample_user.account.borrow_book(sample_book)
            assert sample_book in sample_user.account.borrowed_books
            assert sample_book.copies == 1


        # critical path: return a borrowed book
        def test_user_return_book(self, sample_user, sample_book):
            sample_user.account.borrow_book(sample_book)
            sample_user.account.return_book(sample_book)
            assert sample_book not in sample_user.account.borrowed_books
            assert sample_book.copies == 2



    @pytest.mark.regression
    class TestTransactionStandAloneRegression:

        # negative case: book unavailable
        def test_user_borrow_unavailable_book(self, sample_user):
            book = Book("Python", "Guido", copies=0)
            with pytest.raises(ValueError):
                sample_user.account.borrow_book(book)

        # negative case: returning a book not borrowed
        def test_user_return_non_borrowed_book(self, sample_user):
            book = Book("Clean Code", "Robert Martin", copies=1)
            with pytest.raises(ValueError):
                sample_user.account.return_book(book)



