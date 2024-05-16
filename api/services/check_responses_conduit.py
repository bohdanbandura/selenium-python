class User:
    def signed_in(self, res):
        if 'username' in res:
            assert res['username'] == 'ronaldyoung', 'Wrong username added'
        else: print('username is absent into user body')
        if 'email' in res:
            assert res['email'] == 'lawrence03@example.org', 'Wrong email added'
        else: print('email is absent into user body')
        if 'token' in res:
            assert len(res['token']) > 0, 'Token is not assigned to user'
        else: print('token is absent into user body')

class Article:
    def response(self, res, actual_data, username):
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
    def response(self, res, actual_data, username):
        if 'id' in res:
            assert len(str(res['id'])) > 0, "Comment id is empty"
        else: print('id is absent into comment body')
        if 'body' in res:
            assert res['body'] == actual_data['comment']['body'], "Comment body is wrong"
        else: print('comment is absent into comment body')
        if 'author' in res:
            assert res['author']['username'] == username, "Comment author is wrong"
        else: print('author is absent into comment body')

