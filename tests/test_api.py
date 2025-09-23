import pytest
import requests


@pytest.mark.smoke
class TestAPISmoke:

    def test_get_single_post(self, specific_post_endpoint, get_request, assert_status_code, assert_post_fields):
        response = get_request(specific_post_endpoint(1))
        assert_status_code(response, 200)
        data = response.json()
        assert_post_fields(data)
        assert data["id"] == 1

    def test_post_creation(self, multiple_posts_endpoint, post_request, post_payload, assert_status_code,
                           assert_post_fields, assert_payload_matches):
        response = post_request(multiple_posts_endpoint, post_payload)
        assert_status_code(response, 201)
        data = response.json()
        assert_post_fields(data)
        assert_payload_matches(post_payload, data)

    def test_delete_post(self, specific_post_endpoint, delete_request, assert_status_code):
        response = delete_request(specific_post_endpoint(1))
        assert_status_code(response, 200)



@pytest.mark.regression
class TestAPIRegression:

    @pytest.mark.parametrize("post_id", [1, 10, 50, 100])
    def test_get_multiple_posts(self, base_url, specific_post_endpoint, get_request, assert_status_code, assert_post_fields, post_id):
        response = get_request(specific_post_endpoint(post_id))
        assert_status_code(response, 200)
        data = response.json()
        assert_post_fields(data)
        assert data["id"] == post_id

    def test_get_multiple_posts_at_once(self, multiple_posts_endpoint, get_request, assert_status_code, assert_post_list_fields):
        response = get_request(multiple_posts_endpoint)
        assert_status_code(response, 200)
        data = response.json()
        assert_post_list_fields(data)

    def test_update_post(self, specific_post_endpoint, put_request, put_payload, assert_status_code, assert_post_fields, assert_payload_matches):
        response = put_request(specific_post_endpoint(1), put_payload)
        assert_status_code(response, 200)
        data = response.json()
        assert_post_fields(data)
        assert_payload_matches(put_payload, data)

    def test_partial_update_post(self, specific_post_endpoint, patch_request, patch_payload, assert_status_code,
                                 assert_post_fields, assert_payload_matches):
        response = patch_request(specific_post_endpoint(1), patch_payload)
        assert_status_code(response, 200)
        data = response.json()
        assert_post_fields(data)
        assert_payload_matches(patch_payload, data)


    def test_handle_invalid_endpoint(self, base_url, get_request, assert_status_code):
        url = f"{base_url}/nonexistent"
        response = get_request(url)
        assert_status_code(response, 404)

    def test_handle_invalid_post_id(self, specific_post_endpoint, get_request, assert_status_code):
        response = get_request(specific_post_endpoint(999999))
        assert_status_code(response, 404)

