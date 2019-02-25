from app import app, api
from app.create.user import Register

from flask import request
from flask_restful import Resource

from app.models import *
from app.rest_api.api_resources.api_decorators import *


@app.route("/api/user/create", methods=["POST"])
@api_require_auth
@api_require_admin
@api_require("first_name", str)
@api_require("last_name", str)
@api_require("email", str) # TODO allow for email validation/checking
@api_require("username", str)
@api_require("password", str)
def rest_create_user():
	report = {}

	# Step 1: Retrieve variables from request
	first_name = request.values.get("first_name")
	last_name = request.values.get("last_name")
	email = request.values.get("email")
	username = request.values.get("username")
	password = request.values.get("password")

	# Step 2: Create the user with the Register class from app.create.user

	new_user_create = Register(first_name, last_name, email, password, username)
	new_user_create.register()

	# Step 3: Return a successful report

	report['msg'] = "The user was created successfully."
	report['status'] = True

	return jsonify(report)


