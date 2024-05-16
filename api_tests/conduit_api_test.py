from services.api.factories.api_factory import ApiFactory
from services.api.factories.check_response_factory import CheckResponseFactory
from services.api.factories.data_factory import DataFactory

from services.api.api_tests_logger import logger

import pytest

@pytest.fixture
def api():
    return ApiFactory()

@pytest.fixture
def check():
    return CheckResponseFactory()

@pytest.fixture
def data():
    return DataFactory()

class TestConduitApi:
    def test_sign_up(self, api: ApiFactory, data: DataFactory):
        user = api.user.sign_up(data.user_sign_up)
        print(user)
        print('User succesfully created')
        logger.info('User succesfully created\n')

    def test_sign_in(self, api: ApiFactory, check: CheckResponseFactory, data: DataFactory):
        user = api.user.sign_in(data.user_sign_in)
        check.user.signed_in(user)
        print('User succesfully signed in')
        logger.info('User succesfully signed in\n')
        
    def test_create_article(self, api: ApiFactory, check: CheckResponseFactory, data: DataFactory):
        user = api.user.sign_in(data.user_sign_in)
        article = api.article.create_article(user['token'], data.create_article)
        check.article.response(article, data.create_article, user['username'])
        print('Article succesfully created')
        logger.info('Article succesfully created\n')
    
    def test_update_article(self, api: ApiFactory, check: CheckResponseFactory, data: DataFactory):
        user = api.user.sign_in(data.user_sign_in)
        article = api.article.create_article(user['token'], data.create_article)
        updated_article = api.article.update_article(user['token'], data.create_article, article['slug'])
        check.article.response(updated_article, data.create_article, user['username'])
        print('Article succesfully updated')
        logger.info('Article succesfully updated\n')
    
    def test_add_comment(self, api: ApiFactory, data: DataFactory, check: CheckResponseFactory):
        user = api.user.sign_in(data.user_sign_in)
        article = api.article.create_article(user['token'], data.create_article)
        comment = api.comment.add_comment(user['token'], data.create_comment, article['slug'])
        check.comment.response(comment, data.create_comment, user['username'])
        print("Comment succesfully created")
        logger.info('Comment succesfully updated\n')
    
    def test_delete_comment(self, api: ApiFactory, data: DataFactory):
        user = api.user.sign_in(data.user_sign_in)
        article = api.article.create_article(user['token'], data.create_article)
        comment = api.comment.add_comment(user['token'], data.create_comment, article['slug'])
        api.comment.delete_comment(user['token'], article['slug'], comment['id'])
        print("Comment succesfully deleted")
        logger.info('Comment succesfully deleted\n')
    
    def test_delete_article(self, api: ApiFactory, data: DataFactory):
        user = api.user.sign_in(data.user_sign_in)
        article = api.article.create_article(user['token'], data.create_article)
        api.article.delete_article(user['token'], article['slug'])
        print("Article succesfully deleted")
        logger.info('Article succesfully deleted\n')
    
    def test_update_user(self, api: ApiFactory, data: DataFactory):
        user = api.user.sign_in(data.user_sign_in)
        updated_user = api.user.update_user(user['token'], data.user_update)
        print(updated_user)
        print("User succesfully updated")
        logger.info('User succesfully updated\n')