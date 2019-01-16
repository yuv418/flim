from app import app, api
from app.create.subresponse import NewSubResponse
from app.create.response import NewResponse

from flask import request
from flask_restful import Resource

from app.models import * 


class CreateResponseResource(Resource):
	"""
	Class to create a response from the REST API.
	This can be either a response or a subresponse, 
	Parameters:
	    content: string (content in the post)
	    parent_response_id OR parent_post_id : int (CANNOT BE BOTH)
	    user_id : int (creator of the post) (ONLY FOR ADMINS TODO)
	Response:
	    status: bool (status of the transaction)
	    msg: string (status message)
	"""

	# SECURITY **TODO** restrict to admins and owners of API keys.
	
	def put(self):
		# Create a report variable
		report = {}

		# Step 1: Retrieve request variables.

		content = request.values.get("content")
		parent_response_id = request.values.get("parent_response_id")
		parent_post_id = request.values.get("parent_post_id")
		user_id = request.values.get("user_id")
		api_key = request.values.get("api_key")

		# Make sure that variables are valid. If not, return a failing report.


		# Both parent_response_id and parent_post_id cannot be set
		
		if parent_response_id and parent_post_id:
			report['msg'] = "Error! You provided both a response ID and a post ID!"
			report['status'] = False
			return report

		
		if content == None:
			report['msg'] = "The content that was provided was invalid."
			report['status'] = False
			return report

		elif parent_response_id:
			if parent_response_id == None:
				report['msg'] = "The response you provided was invalid."
				report['status'] = False
				return report

		elif parent_post_id:
			if parent_post_id == None:
				report['msg'] = "The post you provided was invalid."
				report['status'] = False
				return report

		elif user_id == None:
			report['msg'] = "The user ID you provided was invalid."
			report['status'] = False
			return report

		
			
		#################### Step 2: Create corresponding objects ####################

		api_user = Users.get_user_from_api_key(api_key)

				
		# Retrieve the user (for admins). If the user is None, then return a failing report. Otherwise set the creator to the api_user

	
		if api_user.is_admin():
			creator = Users.query.filter_by(id=user_id).first()
			if creator == None:
				report['msg'] = "The user you provided was invalid."
				report['status'] = False
				return report
		else:
			creator = api_user
		
		# First check if parent_post_id is set or parent_response_id is set, and create corresponding objects for them. If the objects are null, in both cases return failing reports.

		
		if parent_post_id:
			parent_post = Post.query.filter_by(id=parent_post_id).first()

			if parent_post == None:
				report['msg'] = "The parent post you provided was invalid."
				report['status'] = False
				return report

		elif parent_response_id:
			parent_response = Response.query.filter_by(id=parent_response_id).first()
			if parent_response == None:
				report['msg'] = "The parent response you provided was invalid."
				report['status'] = False
				return report

		#################### Step 3: Add the response ####################

		# Use NewResponse or NewSubResponse accordingly to add the response.
		
		if parent_post_id:
			# Response, not SubResponse

			new_response = NewResponse(user=creator, parent_post=parent_post, content=content)
			new_response.add_response()

		elif parent_response_id:
			# SubResponse, not Response
			new_subresponse = NewSubResponse(creator=creator, parent_response=parent_response, content=content)

			new_subresponse.create_subpresponse()

		#################### Step 4: Return a successful report. ####################

		# Return appropriate message for each type of response.
		
		if parent_post_id:
			report['msg'] = "The response was created successfully."
		elif parent_response_id:
			report['msg'] = "The subresponse was created successfully."
	
		report['status'] = True
		return report
		
api.add_resource(CreateResponseResource, "/api/response/create")
