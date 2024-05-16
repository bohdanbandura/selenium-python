from resources.api.data_generator import ConduitUser, ConduitArticle

class DataFactory:
    def __init__(self):
        self.user = ConduitUser()
        self.article = ConduitArticle()
        self.user_sign_up = self.user.sign_up_body()
        self.user_sign_in = self.user.existing_user
        self.user_update = self.user.update_body()
        self.create_article = self.article.create_body()
        self.create_comment = self.article.add_comment()
        