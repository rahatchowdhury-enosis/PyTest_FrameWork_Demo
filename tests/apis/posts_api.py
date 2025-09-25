from .base_api import BaseApi


class PostsApi(BaseApi):

    def list_posts(self):
        return self.get("/posts")

    def get_post(self, post_id: int):
        return self.get(f"/posts/{post_id}")

    def create_post(self, payload: dict):
        return self.post("/posts", json=payload)

    def update_post(self, post_id: int, payload: dict):
        return self.put(f"/posts/{post_id}", json=payload)

    def patch_post(self, post_id: int, payload: dict):
        return self.patch(f"/posts/{post_id}", json=payload)

    def delete_post(self, post_id: int):
        return self.delete(f"/posts/{post_id}")
