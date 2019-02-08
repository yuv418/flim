from app.models import *
from app import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users

class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post
