import pytest
from .fixtures.calculator_fixtures import calc
from .fixtures.library_fixtures import (
    sample_user,
    sample_book,
    single_book,
    multiple_books,
    library_users,
    get_book_by_title,
    get_book_by_title_and_author,
)
from .fixtures.payload_fixtures import post_payload, put_payload, patch_payload
from tests.apis.posts_api import PostsApi


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def posts_api():
    """Provides a reusable API client for /posts endpoints."""
    return PostsApi(base_url=BASE_URL)
