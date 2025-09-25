import requests


class BaseApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint, **kwargs):
        return requests.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, json=None):
        return requests.post(f"{self.base_url}{endpoint}", json=json)

    def put(self, endpoint, json=None):
        return requests.put(f"{self.base_url}{endpoint}", json=json)

    def patch(self, endpoint, json=None):
        return requests.patch(f"{self.base_url}{endpoint}", json=json)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}")
