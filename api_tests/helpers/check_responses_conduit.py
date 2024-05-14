class User:
    def check_user_signed_in_and_up(res, actual_data):
        if 'username' in res:
            assert res['username'] == actual_data['user']['username'], 'Wrong username added'
        else: print('username is absent into user body')
        if 'email' in res:
            assert res['email'] == actual_data['user']['email'], 'Wrong email added'
        else: print('email is absent into user body')
        if 'token' in res:
            assert len(res['token']) > 0, 'Token is not assigned to user'
        else: print('token is absent into user body')

class Article:
    def check_article_response(res, actual_data, username):
        if 'slug' in res:
            assert len(res['slug']) > 0, 'Slug is not assigned to article'
        else: print('slug is absent into article body')
        if 'body' in res:
            assert res['body'] == actual_data['article']['body'], 'Wrong body added'
        else: print('body is absent into article body')
        if 'author' in res:
            assert res['author']['username'] == username, 'Wrong author added'
        else: print('author is absent into article body')

class Comment:
    def check_comment_response(res, actual_data, username):
        if 'id' in res:
            assert len(str(res['id'])) > 0, "Comment id is empty"
        else: print('id is absent into comment body')
        if 'body' in res:
            assert res['body'] == actual_data['comment']['body'], "Comment body is wrong"
        else: print('comment is absent into comment body')
        if 'author' in res:
            assert res['author']['username'] == username, "Comment author is wrong"
        else: print('author is absent into comment body')

