from app.models import *
from app import ma


class UserSchema(ma.ModelSchema):
	class Meta:
		fields = ('about', 'id', 'first_name', 'last_name', 'email', 'groups', 'post', 'response')
		model = Users


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post

class GroupSchema(ma.ModelSchema):
	class Meta:
		model = Group
