from app import app, api, db
from app.models import *

from flask import request
from flask_restful import Resource


class DeleteUserResource(Resource):
	"""
	DeleteUserResource is a Resource that allow you to delete a user. This resource's function can only be performed by the user with the API key or an administrator.
	Parmeters:
	   user_id: int
	Responses:
	   status: bool
	   msg: string
	"""

	
	def delete(self):
		""" Deletes a user from their user_id. Returns a status message at the end."""
		# Create a report variable.
		report = {}

		# Step 1: Retrieve variables from request.

		user_id = request.values.get("user_id")
		api_key = request.values.get("api_key")

		# Step 2: Perform validation of variables (make sure they exist)


		if user_id == None:
			report['msg'] = "The user ID you provided was invalid."
			report['status'] = False

			return report
			

		# Step 3: Retrieve models from request data and make sure they are valid.
		
		user_to_delete = Users.query.filter_by(id=user_id).first()
		api_user = Users.get_user_from_api_key(api_key)

		if user_to_delete == None:	

			report['msg'] = "The user ID you provided was invalid."
			report['status'] = False

			return report
		


		# Step 4:
		# Make sure the users are the same or the api user is an administrator.
		# If they are, delete the user. Otherwise, return a failing report.
		
		if api_user.is_admin() or api_user == user_to_delete:
			db.session.delete(user_to_delete)
			db.session.commit()
		else:
			# Return a failing report about privileges.
			report['msg'] = "You do not have sufficient privileges to perform this task."
			report['status'] = False

			return report
		
		# Step 5: Everything went well. Return a successful report.
		
		report['msg'] = "The user was deleted successfully."
		report['status'] = False

		return report
		
		


api.add_resource(DeleteUserResource, "/api/user/delete")
		
