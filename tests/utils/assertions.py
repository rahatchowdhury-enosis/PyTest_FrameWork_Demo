class AssertData:

    @staticmethod
    def status_code(response, expected):
        assert response.status_code == expected

    @staticmethod
    def has_post_fields(data):
        assert isinstance(data, dict)
        for field in ["id", "userId", "title", "body"]:
            assert field in data

    @staticmethod
    def payload_matches(payload, response_json, exclude=None):
        """
        Assert all keys/values in payload match response_json.
        Optionally exclude some keys (like auto-generated 'id').
        """

        exclude = exclude or []
        for key, value in payload.items():
            if key not in exclude:
                assert response_json[key] == value, f"Mismatch for key '{key}'"

    @staticmethod
    def has_post_list_fields(data, min_count=1):
        assert isinstance(data, list)
        assert len(data) >= min_count
        for post in data[:min_count]:
            for field in ["id", "userId", "title", "body"]:
                assert field in post
