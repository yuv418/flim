from app import app, api
from flask import request
from flask_restful import Resource

from app.models import *
from app.schemas import *
from app.rest_api.api_resources.api_decorators import *
class UserByIDResource(Resource):
	def get(self, user_id):
		user = Users.query.filter_by(id=user_id).first()
		return user.as_dict()

class UserByUsernameResource(Resource):
	def get(self, user_name):
		user = Users.query.filter_by(username=user_name).first()
		return user.as_dict()

class UserByFirstNameResource(Resource):
	def get(self, first_name):
		users = Users.query.filter_by(first_name=first_name).all()
		return get_id_list(users)

class UserByLastNameResource(Resource): # Return a list of user IDs for each person with the same first name
	def get(self, last_name):
		users = Users.query.filter_by(last_name=last_name).all()
		return get_id_list(users)


class UserByLastNameResource(Resource):  # Return a list of user IDs for each person with the same last name
	def get(self, last_name):
		users = Users.query.filter_by(last_name=last_name).all()
		return get_id_list(users)

class UserByEmailResource(Resource):  # Return a list of user IDs for each person with the same e-mail 
	def get(self, email):
		users = Users.query.filter_by(email=email).all()
		return get_id_list(users)

@app.route("/api/user/all")
@api_require_auth
def rest_user_all():
	userschema = UserSchema(many=True)
	all_users = Users.query.all()
	return userschema.jsonify(all_users)


api.add_resource(UserByIDResource, "/api/user/by-id/<user_id>")
api.add_resource(UserByUsernameResource, "/api/user/by-username/<user_name>")
api.add_resource(UserByFirstNameResource, "/api/user/by-first_name/<first_name>")
api.add_resource(UserByLastNameResource, "/api/user/by-last_name/<last_name>")
api.add_resource(UserByEmailResource, "/api/user/by-email/<email>")

