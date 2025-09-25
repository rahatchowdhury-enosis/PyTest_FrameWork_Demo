import pytest
from src.transactions import Transaction


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
        @pytest.mark.parametrize(
            "book_specs, fees, expected_balance",
            [
                ([("Book 1", "Author 1", 2), ("Book 2", "Author 2", 1)], [10, 15], 75),
                ([("Book A", "Author A", 1)], [5], 95),
                ([("Book X", "Author X", 3), ("Book Y", "Author Y", 2)], [20, 10], 70),
            ],
        )
        def test_multiple_books_and_fees_cases(
            self, sample_user, multiple_books, book_specs, fees, expected_balance
        ):
            books = multiple_books(*book_specs)
            for book in books:
                sample_user.account.borrow_book(book)

            txn = Transaction(sample_user)
            for fee in fees:
                txn.charge_late_fee(fee)

            assert sample_user.balance == expected_balance

        # edge case: borrowing same book twice
        @pytest.mark.parametrize(
            "title, author, copies",
            [
                ("Duplicate", "Author", 1),
                ("Python 101", "Guido", 1),
                ("Learn Pytest", "Tester", 1),
            ],
        )
        def test_edge_case_borrow_same_book_with_one_copy_param(
            self, sample_user, single_book, title, author, copies
        ):
            book = single_book(title=title, author=author, copies=copies)
            sample_user.account.borrow_book(book)

            with pytest.raises(ValueError):
                sample_user.account.borrow_book(book)

        # edge case: returning a book never borrowed
        @pytest.mark.parametrize(
            "title, author, copies",
            [
                ("Not Borrowed", "Author", 1),
                ("Random Book", "Guido", 2),
                ("Ghost Book", "Tester", 3),
            ],
        )
        def test_edge_case_return_not_borrowed_param(
            self, sample_user, single_book, title, author, copies
        ):
            book = single_book(title=title, author=author, copies=copies)

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
        @pytest.mark.parametrize(
            "title, author, copies",
            [
                ("Python", "Guido", 0),
                ("Clean Code", "Robert Martin", 0),
                ("Learn Pytest", "Tester", 0),
            ],
        )
        def test_user_borrow_unavailable_book_param(
            self, sample_user, single_book, title, author, copies
        ):
            book = single_book(title=title, author=author, copies=copies)

            with pytest.raises(ValueError):
                sample_user.account.borrow_book(book)

        # negative case: returning a book not borrowed
        @pytest.mark.parametrize(
            "title, author, copies",
            [
                ("Clean Code", "Robert Martin", 1),
                ("Python 101", "Guido", 1),
                ("Learn Pytest", "Tester", 2),
            ],
        )
        def test_user_return_non_borrowed_book_param(
            self, sample_user, single_book, title, author, copies
        ):
            book = single_book(title=title, author=author, copies=copies)

            with pytest.raises(ValueError):
                sample_user.account.return_book(book)
