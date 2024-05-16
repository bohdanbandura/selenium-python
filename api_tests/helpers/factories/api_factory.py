from helpers.conduit_requests import UserApi, ArticleApi, CommentApi

class ApiFactory():
    def __init__(self):
        self.user = UserApi()
        self.article = ArticleApi()
        self.comment = CommentApi()