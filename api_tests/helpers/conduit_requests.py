from api_tests.helpers.base_api import BaseApi

class UserApi(BaseApi):
    def __init__(self):
        super().__init__()
        
    def sign_up(self, body):
        return self.post("users", body)
            
    def sign_in(self, body):
        return self.post("users/login", body)['user']
            
    def update_user(self, token, body):
        self.headers['Authorization'] = f"Token {token}"
        body['user']['token'] = token
        return self.put("user", body, headers=self.headers)['user']
             
class ArticleApi(BaseApi):
    def __init__(self):
        super().__init__()
        
    def create_article(self, token, body):
        self.headers['Authorization'] = f"Token {token}"
        return self.post("articles", body, headers=self.headers)['article']
            
    def update_article(self, token, body, article_slug):
        self.headers['Authorization'] = f"Token {token}"
        return self.put(f"articles/{article_slug}", body, headers=self.headers)['article']
            
    def delete_article(self, token, article_slug):
        self.headers['Authorization'] = f"Token {token}"
        return self.delete(f"articles/{article_slug}", headers=self.headers, status_code=204)
            
class CommentApi(BaseApi):
    def __init__(self):
        super().__init__()
        
    def add_comment(self, token, body, article_slug):
        self.headers['Authorization'] = f"Token {token}"
        return self.post(f"articles/{article_slug}/comments", body, headers=self.headers)['comment']
            
    def delete_comment(self, token, article_slug, comment_id):
        self.headers['Authorization'] = f"Token {token}"
        return self.delete(f"articles/{article_slug}/comments/{comment_id}", headers=self.headers, status_code=204)
    