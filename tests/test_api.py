import pytest
import requests

from tests.utils.assertions import AssertData


@pytest.mark.smoke
class TestAPISmoke:

    def test_get_single_post(self, posts_api):
        response = posts_api.get_post(1)
        AssertData.status_code(response, 200)

        data = response.json()
        AssertData.has_post_fields(data)
        assert data["id"] == 1

    def test_post_creation(self, post_payload, posts_api):
        response = posts_api.create_post(post_payload)
        AssertData.status_code(response, 201)

        data = response.json()
        AssertData.has_post_fields(data)
        AssertData.payload_matches(post_payload, data)

    def test_delete_post(self, posts_api):
        response = posts_api.delete_post(1)
        AssertData.status_code(response, 200)


@pytest.mark.regression
class TestAPIRegression:

    @pytest.mark.parametrize("post_id", [1, 10, 50, 100])
    def test_get_multiple_posts(self, posts_api, post_id):
        response = posts_api.get_post(post_id)
        AssertData.status_code(response, 200)

        data = response.json()
        AssertData.has_post_fields(data)
        assert data["id"] == post_id

    def test_get_multiple_posts_at_once(self, posts_api):
        response = posts_api.list_posts()
        AssertData.status_code(response, 200)
        data = response.json()
        AssertData.has_post_list_fields(data)

    def test_update_post(self, put_payload, posts_api):
        response = posts_api.update_post(1, put_payload)
        AssertData.status_code(response, 200)
        data = response.json()
        AssertData.has_post_fields(data)
        AssertData.payload_matches(put_payload, data)

    def test_partial_update_post(self, patch_payload, posts_api):
        response = posts_api.patch_post(1, patch_payload)
        AssertData.status_code(response, 200)
        data = response.json()
        AssertData.has_post_fields(data)
        AssertData.payload_matches(patch_payload, data)

    def test_handle_invalid_endpoint(self, posts_api):
        response = posts_api.get("/nonexistent")
        AssertData.status_code(response, 404)

    def test_handle_invalid_post_id(self, posts_api):
        response = posts_api.get_post(999999)
        AssertData.status_code(response, 404)
