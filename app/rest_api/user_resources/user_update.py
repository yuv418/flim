from app import app, api, db
from app.models import *

from flask import request
from flask_restful import Resource


# Update a user. TODO implement this only for the API user and admins.
class UpdateUserResource(Resource):
	"""
	UpdateUserResource is a Resource to allow you to update a user.
	Parameters:
	    user_id: int
	    (the following are optional, you must include at least one)
	    first_name
	    last_name
	    email
	    about
	    password
    Response:
	    status: bool
	    msg: str
	"""

	def put(self):
		# Create a status variable.

		report = {}

		# Step 1: Retrieve request parameters:

		user_id = request.values.get("user_id")
		first_name = request.values.get("first_name")
		last_name = request.values.get("last_name")
		email = request.values.get("email")
		about = request.values.get("about")
		password = request.values.get("password")


		
		# Step 2: Perform basic form validation.

		if user_id == None:
			report['msg'] = "The user ID you provided was invalid."
			report['status'] = False
			return report
		elif first_name == None or last_name == None or email == None or about == None or password == None:
			report['msg'] = "You must provide at least one value to alter."
			report['status'] = False
			return report

		
		# Step 3: retrieve the user and update their corresponding properties.
		
		user_to_update = User.query.filter_by(id=user_id).first()

		if first_name:
			user_to_update.first_name = first_name
		if last_name:
			user_to_update.last_name = last_name
		if email:
			user_to_update.email = email
		if about:
			user_to_update.about = about
		if password:
			user_to_update.set_password(password)

		# Commit the changes made.

		db.session.commit()

		# Since these changes have been made successfully, return a sucessful report.

		report['msg'] = "The user was updated successfully."
		report['status'] = True

		return report


api.add_resource(UpdateUserResource, "/api/user/update")

			


		

	
	
	

