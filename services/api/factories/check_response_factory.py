from services.api.check_responses_conduit import User, Article, Comment

class CheckResponseFactory:
    def __init__(self):
        self.user = User()
        self.article = Article()
        self.comment = Comment()