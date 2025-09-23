import pytest
from src.user import User
from src.library import Book, LibraryAccount
from src.calculator import Calculator
import requests

# ------------------------
# Calculator fixture
# ------------------------
@pytest.fixture
def calc():
    """Returns a Calculator instance"""
    return Calculator()

# ------------------------
# Sample user fixture
# ------------------------
@pytest.fixture
def sample_user():
    """Returns a User instance with default balance and LibraryAccount"""
    return User("alice", balance=100)

# ------------------------
# Sample book fixture
# ------------------------
@pytest.fixture
def sample_book():
    """Returns a Book instance"""
    return Book("1984", "George Orwell", copies=2)


@pytest.fixture
def get_book_by_title():
    def _get(account, title):
        return next(b for b in account.borrowed_books if b.title == title)
    return _get

@pytest.fixture
def get_book_by_title_and_author():
    def _get(account, title, author):
        return next(b for b in account.borrowed_books if (b.title == title and b.author == author))
    return _get


# ------------------------
# Library users from JSON
# ------------------------
@pytest.fixture
def library_users():
    """
    Returns a list of LibraryAccount instances for testing.
    Alice already has "Python 101".
    Bob starts with no books.
    """
    # Alice with one borrowed book
    alice = LibraryAccount("Alice")
    borrowedBooks = Book("Python 101", "Guido", copies=1)
    alice.borrow_book(borrowedBooks)

    # Bob with no borrowed books
    bob = LibraryAccount("Bob")
    bob.borrowed_books = []

    return [alice, bob]


# Base URL for all tests
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def specific_post_endpoint(base_url):
    def _make(post_id=None):
        if post_id:
            return f"{base_url}/posts/{post_id}"
        return f"{base_url}/posts"
    return _make


# Example multiple posts endpoint
@pytest.fixture
def multiple_posts_endpoint(base_url):
    return f"{base_url}/posts"


# Example payload for POST / PUT / PATCH
@pytest.fixture
def post_payload():
    return {"title": "foo", "body": "bar", "userId": 1}

@pytest.fixture
def put_payload():
    return {"id": 1, "title": "updated", "body": "updated body", "userId": 1}

@pytest.fixture
def patch_payload():
    return {"title": "patched title"}

@pytest.fixture
def get_request():
    def _get(url):
        return requests.get(url)
    return _get

@pytest.fixture
def post_request():
    def _post(url, json_body):
        return requests.post(url, json=json_body)
    return _post

@pytest.fixture
def put_request():
    def _put(url, json_body):
        return requests.put(url, json=json_body)
    return _put

@pytest.fixture
def patch_request():
    def _patch(url, json_body):
        return requests.patch(url, json=json_body)
    return _patch

@pytest.fixture
def delete_request():
    def _delete(url):
        return requests.delete(url)
    return _delete

@pytest.fixture
def assert_status_code():
    def _assert(response, expected):
        assert response.status_code == expected
    return _assert

@pytest.fixture
def assert_post_fields():
    def _assert(data):
        assert isinstance(data, dict)
        assert "id" in data
        assert "userId" in data
        assert "title" in data
        assert "body" in data
    return _assert

@pytest.fixture
def assert_payload_matches():
    def _assert(payload, response_json, exclude_keys=None):
        """
        Assert all keys/values in payload match response_json.
        Optionally exclude some keys (like auto-generated 'id').
        """
        exclude_keys = exclude_keys or []
        for key, value in payload.items():
            if key not in exclude_keys:
                assert response_json[key] == value, f"Mismatch for key '{key}'"
    return _assert

@pytest.fixture
def assert_post_list_fields():
    def _assert(data, n=5):
        assert isinstance(data, list)
        assert len(data) > 0
        for post in data[:n]:
            assert "id" in post
            assert "userId" in post
            assert "title" in post
            assert "body" in post
    return _assert


