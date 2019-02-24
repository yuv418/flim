from app import app, api
from flask import request
from flask_restful import Resource

from app.models import *
from app.schemas import *
from app.rest_api.api_resources.api_decorators import *

@app.route("/api/user/<field>/<value>")
@api_require_auth
def rest_user_by_field(field, value):
	"""Filter a user by field and value"""
	# Retrieve all models with the schema and filter
	userschema = UserSchema(many=True)
	all_users = Users.query.all()
	users_list = userschema.dump(all_users).data

	# Filter the users, handle if field is invalid

	try:
		filtered_users = []
		for user in users_list:
			if str(user[field]) == value:
				filtered_users.append(user)
	except KeyError:
		return jsonify({"status": False, "msg": "Invalid field."}), 400

	# Return filtered users unless field is ID, then just return one user.

	if field == "id" and len(filtered_users) != 0:
		return jsonify(filtered_users[0])

	return jsonify(filtered_users)

@app.route("/api/user/all")
@api_require_auth
def rest_user_all():
	userschema = UserSchema(many=True)
	all_users = Users.query.all()
	return userschema.jsonify(all_users)


