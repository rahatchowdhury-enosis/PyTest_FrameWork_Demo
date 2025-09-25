import pytest


@pytest.fixture
def post_payload():
    return {"title": "foo", "body": "bar", "userId": 1}


@pytest.fixture
def put_payload():
    return {"id": 1, "title": "updated", "body": "updated body", "userId": 1}


@pytest.fixture
def patch_payload():
    return {"title": "patched title"}
