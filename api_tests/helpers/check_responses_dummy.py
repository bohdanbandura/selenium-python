class Post:
    def check_known_post_response(res, actual_data, actual_user):
        if 'owner' in res:
            assert res['owner']['id'] == actual_user['id'], 'Wrong owner assigned to the post'
        else: print('owner is absent into post body')
        if 'text' in res:
            assert res['text'] == actual_data['text'], 'Wrong text populated in the post'
        else: print('text is absent into post body')
        if 'image' in res:
            assert res['image'] == actual_data['image'], 'Wrong image populated in the post'
        else: print('image is absent into post body')

    def check_unknown_post_response(res):
        for post in res['data']:
            if 'owner' in post:
                assert len(post['owner']['id']) > 0, "Post owner id is empty"
            else: print('owner is absent into post body')
            if 'text' in post:
                assert len(post['text']) > 0, "Post text is empty"
            else: print('text is absent into post body')
            if 'likes' in post:
                assert post['likes'] >= 0, "Post likes is not present"
            else: print('likes is absent into post body')
            
    def check_post_update(res, actual_data):
        if 'text' in res:
            assert res['text'] == actual_data['text'], 'Wrong text populated in the post'
        else: print('text is absent into post body')
        if 'tags' in res:
            assert res['tags'] == actual_data['tags'], 'Wrong tags populated in the post'
        else: print('tags is absent into post body')
        
        
class User:
    def check_unknown_user_response(res):
        for user in res['data']:
            if 'id' in user: 
                assert len(user['id']) > 0, "User id is empty"
            else: print('id is absent into user body')
            if 'firstName' in user: 
                assert len(user['firstName']) > 0, "User first name is empty"
            else: print('first name is absent into user body')
            if 'lastName' in user: 
                assert len(user['lastName']) > 0, "User last name is empty"
            else: print('last name is absent into user body')
            if 'email' in user: 
                assert len(user['email']) > 0,  "User email is empty"
            else: print('email is absent into user body')
            
    def check_known_user_response(res, actual_data):
        if 'id' in res: 
            assert len(res['id']) > 0, "User id is empty"
        else: print('id is absent into user body')
        if 'firstName' in res: 
            assert res['firstName'] == actual_data['firstName'], "User first populated wrong way" 
        else: print('first name is absent into user body')
        if 'lastName' in res: 
            assert res['lastName'] == actual_data['lastName'], "User last name populated wrong way"
        else: print('last name is absent into user body')
        if 'firstName' in res: 
            assert res['email'] == actual_data['email'],  "User email populated wrong way"
        else: print('email is absent into user body')
        
    def check_user_update(res, actual_data):
        if 'firstName' in res: 
            assert res['firstName'] == actual_data['firstName'], "User first populated wrong way"
        else: print('first name is absent into user body')
        if 'lastName' in res: 
            assert res['lastName'] == actual_data['lastName'], "User last name populated wrong way"
        else: print('last name is absent into user body')
        
        
class Comment:
    def check_unknown_comment_response(res):
        for comment in res['data']:
            if 'id' in comment:
                assert len(comment['id']) > 0, "Comment id is empty"
            else: print('id is absent into comment body')
            if 'message' in comment:
                assert len(comment['message']) > 0, "Comment message is empty"
            else: print('message is absent into comment body')
            if 'owner' in comment:
                assert len(comment['owner']['id']) > 0, "Comment owner id is empty"
            else: print('owner is absent into comment body')
            
    def check_known_comment_response(res, actual_data):
        if 'id' in res:
            assert len(res['id']) > 0, 'Wrong comment returned'
        else: print('id is absent into comment body')
        if 'message' in res:
            assert res['message'] == actual_data['message'], 'Wrong comment returned'
        else: print('message is absent into comment body')
        if 'owner' in res:
            assert res['owner']['id'] == actual_data['owner'], 'Wrong comment returned'
        else: print('owner is absent into comment body')
        if 'post' in res:
            assert res['post'] == actual_data['post'], 'Wrong comment returned'
        else: print('post is absent into comment body') 