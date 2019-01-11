from app import app, api
from app.create.user import Register

from flask import request
from flask_restful import Resource

from app.models import * 

# TODO: Only allow admins to perform this task and make this happen without a check in **each and every class** it needs to be checked.

class CreateUserResource(Resource):
	"""
	CreateUserResource is a class to insert a user into the database.
	Paramters:
	    first_name: The first name of the user
	    last_name: THe last name of the user
	    email: The e-mail of the user
	    username: The username of the user
	    password: The password of the user
	Returns:
	    status: boolean that states whether the transaction was successful or not
	    msg: string that is the status message for the transaction
	"""
	
	def get(self):
		# Create a report variable
		report = {}

		# Step 1: Retrieve variables from request
		first_name = request.values.get("first_name")
		last_name = request.values.get("last_name")
		email = request.values.get("email")
		username = request.values.get("username")
		password = request.values.get("password")
		
		# Step 2: Validate the inputted values to see if any are blank. They cannot be.

		if password  == None:

			# The username is blank. Return a failing report.

			report['msg'] = "The password cannot be blank."
			report['status'] = False

			return report

		
		if first_name == None:

			# The first name is blank. Return a failing report.

			report['msg'] = "The first name cannot be blank."
			report['status'] = False

			return report

		if last_name == None:

			# The last name is blank. Return a failing report.

			report['msg'] = "The last name cannot be blank."
			report['status'] = False

			return report

		if email == None:

			# The email is blank. Return a failing report.

			report['msg'] = "The e-mail cannot be blank."
			report['status'] = False

			return report

		if username == None:

			# The username is blank. Return a failing report.

			report['msg'] = "The username cannot be blank."
			report['status'] = False

			return report


		# Step 3: Create the user with the Register class from app.create.user

		new_user_create = Register(first_name, last_name, email, password, username)
		new_user_create.register()

		# Step 4: Return a successful report

		report['msg'] = "The user was created successfully."
		report['status'] = True

		return report

api.add_resource(CreateUserResource, "/api/user/create")
