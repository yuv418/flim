from app import app, api
from flask import request
from flask_restful import Resource

from app.models import * 

class UserByIDResource(Resource):
	def get(self, user_id):
		user = Users.query.filter_by(id=user_id).first()
		return user.as_dict()
		
class UserByUsernameResource(Resource):
	def get(self, user_name):
		user = Users.query.filter_by(username=user_name).first()
		return user.as_dict()
	

api.add_resource(UserByIDResource, "/api/user/by-id/<user_id>")
api.add_resource(UserByUsernameResource, "/api/user/by-username/<user_name>")
