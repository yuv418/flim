from app.models import *
from app import ma


class UserSchema(ma.ModelSchema):
	class Meta:
		fields = ('id', 'first_name', 'last_name', 'email', 'about', 'username')
		model = Users

class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post

