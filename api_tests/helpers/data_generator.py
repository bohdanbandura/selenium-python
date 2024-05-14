from faker import Faker

def create_tags():
    tags = []
    for _ in range(5):
        tags.append(Faker().word())
    return tags

user_create_body = {
    "title": "mr",
    "firstName": Faker().first_name(),
    "lastName": Faker().last_name(),
    "gender": "male",
    "email": Faker().email(),
    "dateOfBirth": "2/9/1999",
}

user_update_body = {
    "firstName": Faker().first_name(),
    "lastName": Faker().last_name()
}

post_create_body = {
    'text': Faker().catch_phrase(),
    'image': Faker().image_url(),
    'likes': 0,
    'tags': ['tag1', 'tag2']
}

post_update_body = {
    'text': Faker().catch_phrase(),
    'tags': create_tags()
}

comment_create_body = {
    'message': Faker().catch_phrase()
}

user_conduit_body = {
    "user": {
        "email": Faker().email(),
        "password": Faker().word(),
        "username": Faker().user_name()
    }
}

user_login_body = {
    "user": {
        "email": "afdsfa@afasdf.com",
        "password": "gdfgdg"
    } 
}

article_conduit_body = {
    "article": {
        "title": Faker().catch_phrase(),
        "description": Faker().text(max_nb_chars=20),
        "body": Faker().text(max_nb_chars=70),
        "tagList": create_tags()
    }
}

comment_conduit_body = {
    "comment": {
        "body": Faker().catch_phrase()
    }
}

user_update_conduit_body = {
    "user": {
        "image": Faker().image_url(),
        "username": Faker().user_name(),
        "bio": Faker().catch_phrase(),
        "email": Faker().email(),
        "token": "",
        "effectiveImage": Faker().image_url()
    }
}