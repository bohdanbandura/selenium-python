from helpers.conduit_requests import get, post, put, delete
from helpers.check_responses_conduit import User, Article, Comment
from api_tests.helpers.data_generator import *

class TestConduitApi:
    def test_sign_up(self):
        response = post("users", user_conduit_body)
        if response.status_code == 200:
            user = response.json()['user']
            User.check_user_signed_in_and_up(user, user_conduit_body)
            print('User succesfully created')

    
    def test_sign_in(self):
        user_login_body['user']['email'] = user_conduit_body['user']['email']
        user_login_body['user']['password'] = user_conduit_body['user']['password']
        response = post("users/login", user_login_body)
        global token
        global username
        if response.status_code == 200:
            user = response.json()['user']
            User.check_user_signed_in_and_up(user, user_conduit_body)
            token = user['token']
            username = user['username']
            print('User succesfully signed in')
        
    def test_create_article(self):
        response = post("articles", article_conduit_body, token=token)
        global article_slug
        if response.status_code == 200:
            article = response.json()['article']
            Article.check_article_response(article, article_conduit_body, username)
            article_slug = article['slug']
            print('Article succesfully created')
    
    def test_update_article(self):
        response = put(f"articles/{article_slug}", article_conduit_body, token=token)
        if response.status_code == 200:
            article = response.json()['article']
            Article.check_article_response(article, article_conduit_body, username)
            print("Article succesfully updated")
    
    def test_add_comment(self):
        response = post(f"articles/{article_slug}/comments", comment_conduit_body, token=token)
        global comment_id
        if response.status_code == 200:
            comment = response.json()['comment']
            Comment.check_comment_response(comment, comment_conduit_body, username)
            comment_id = response.json()['comment']['id']
            print("Comment succesfully created")
    
    def test_delete_comment(self):
        response = delete(f"articles/{article_slug}/comments/{comment_id}", token=token)
        if response.status_code == 204:
            print("Comment succesfully deleted")
    
    def test_delete_article(self):
        response = delete(f"articles/{article_slug}", token=token)
        if response.status_code == 204:
            print("Article succesfully deleted")
    
    def test_update_user(self):
        user_update_conduit_body['user']['token'] = token
        response = put("user", user_update_conduit_body, token=token)
        updated_user = response.json()['user']
        if response.status_code == 200:
            print("User succesfully updated")