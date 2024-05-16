from faker import Faker
from dataclasses import dataclass, asdict, field

def create_tags():
    tags = []
    for _ in range(5):
        tags.append(Faker().word())
    return tags    

@dataclass
class ConduitUser:
    email: str = field(default_factory=lambda: Faker().email())
    password: str = field(default_factory=lambda: Faker().password())
    username: str = field(default_factory=lambda: Faker().user_name())
    image: str = field(default_factory=lambda: Faker().image_url())
    bio: str = field(default_factory=lambda: Faker().catch_phrase())
    token: str = ''
    effectiveImage: str = field(default_factory=lambda: Faker().image_url())
    existing_user: dict = field(default_factory=lambda: {
        'user': {
            'email': 'lawrence03@example.org', 
            'password': 'drop'
        }
    })
    
    def sign_up_body(self):
        return {
            'user': {
                'email': self.email,
                'password': self.password,
                'username': self.username
            }
        }
        
    def update_body(self):
        return {
            'user': {
                'image': self.image,
                'bio': self.bio,
                'token': self.token,
                'effectiveImage': self.effectiveImage
            }
        }
    
@dataclass
class ConduitArticle:
    title: str = field(default_factory=lambda: Faker().catch_phrase())
    description: str = field(default_factory=lambda: Faker().text(max_nb_chars=20))
    body: str = field(default_factory=lambda: Faker().text(max_nb_chars=70))
    tagList: list = field(default_factory=lambda: create_tags())
    comment: str = field(default_factory=lambda: Faker().catch_phrase())
    
    def create_body(self):
        return {
            'article': {
                'title': self.title,
                'description': self.description,
                'body': self.body,
                'tagList': self.tagList
            }
        }
        
    def add_comment(self):
        return {
            "comment": {
                "body": self.comment
            }
        }
        