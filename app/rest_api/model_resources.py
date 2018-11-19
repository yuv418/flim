from app import app, api
from flask import request
from flask_restful import Resource

from app.models import *

class UserResource(Resource):
	def get(self, user_id):
		user = Users.query.filter_by(id=user_id).first()
		return user.as_dict()
		
		
		
api.add_resource(UserResource, "/api/user/<user_id>")
		
		
	
