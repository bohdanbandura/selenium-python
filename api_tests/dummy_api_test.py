from api_tests.helpers.data_generator import *

from api_tests.helpers.check_responses_dummy import User, Post, Comment
from api_tests.helpers.dummy_requests import get, post, put, delete

class TestDummyApi:
    
    def test_get_all_users(self):
        response = get("user")
        if response.status_code == 200:
            users = response.json()
            print("Users succesfully received")
            User.check_unknown_user_response(users)
                
    def test_get_all_posts(self):
        response = get("post")
        if response.status_code == 200:
            posts = response.json()
            print("Posts succesfully received")
            Post.check_unknown_post_response(posts)
            
    def test_get_all_comments(self):
        response = get("comment")
        if response.status_code == 200:
            comments = response.json()
            print("Comments succesfully received")
            Comment.check_unknown_comment_response(comments)
                    
    def test_add_new_user(self):
        response = post("user/create", user_create_body)
        global user_data
        if response.status_code == 200:
            user_data = response.json()
            User.check_known_user_response(user_data, user_create_body)
            print("User succesfully added")
            
            
    def test_update_user(self):
        response = put(f"user/{user_data['id']}", user_update_body)
        if response.status_code == 200:
            user = response.json()
            User.check_user_update(user, user_update_body)
            print("User succesfully updated")
        
        
    def test_add_new_post(self):
        post_create_body['owner'] = user_data['id']
        response = post("post/create", post_create_body)
        global post_data
        if response.status_code == 200:
            post_data = response.json()
            Post.check_known_post_response(post_data, post_create_body, user_data)
            print("Post succesfully added")
            
        
    def test_get_posts_by_user_id(self):
        response = get(f"user/{user_data['id']}/post")
        if response.status_code == 200:
            post = response.json()
            if 'data' in post:
                assert post['data'][0]['id'] == post_data['id'], 'Wrong post returned'
                print("Post succesfully found by user id")


    def test_update_post(self):
        response = put(f"post/{post_data['id']}", post_update_body)
        if response.status_code == 200:
            post = response.json()
            Post.check_post_update(post, post_update_body)
            print("Comment succesfully updated")   
            
    
    def test_add_new_comment(self):
        comment_create_body['owner'] = user_data['id']
        comment_create_body['post'] = post_data['id']
        response = post("comment/create", comment_create_body)
        global comment_data
        if response.status_code == 200:
            comment_data = response.json()
            Comment.check_known_comment_response(comment_data, comment_create_body)
            print("Comment succesfully added")
            
            
    def test_delete_comment(self):
        response = delete(f"comment/{comment_data['id']}")
        if response.status_code == 200:
            res = response.json()
            assert res['id'] == comment_data['id'], 'Wrong comment deleted'
            print("Comment succesfully deleted")
    
    
    def test_delete_post(self):
        response = delete(f"post/{post_data['id']}")
        if response.status_code == 200:
            res = response.json()
            assert res['id'] == post_data['id'], 'Wrong post deleted'
            print("Post succesfully deleted")
        

    def test_delete_user(self):
        response = delete(f"user/{user_data['id']}")
        if response.status_code == 200:
            res = response.json()
            assert res['id'] == user_data['id'], 'Wrong user deleted'
            print("User succesfully deleted")
        
        
    def test_get_user_by_id(self):
        response = get(f"user/{user_data['id']}")
        if response.status_code == 200:
            res = response.json()
            assert res['error'] == 'RESOURCE_NOT_FOUND'