
class PostsAPI:
    def __init__(self,client):
        self.client = client
        self.base = 'https://jsonplaceholder.typicode.com'
    def get_post(self,post_id):
        return self.client.get(f'{self.base}/posts/{post_id}')

    def get_posts_by_user(self,user_id):
        return self.client.get(f'{self.base}/posts', params={'userId': user_id})
