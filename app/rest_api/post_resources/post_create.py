from app import app, api
from app.models import *
from app.create.post import NewPost

from flask import request
from flask_restful import Resource

class CreatePostResoruce(Resource):
	""" 
	A resource that allows you to create a post from the REST API.
	Takes parameters: 
	    user_id: int
	    title: string
	    content: string
	    topics: list separated by the ',' character.
	Returns: 
	    status: boolean
	    msg: string
	    post_id: int (id of new post)
	"""
	def put(self):

		# Create a report variable to return to the user at the end.
		report = {}
		

		# Step 1: retrieve parameters

		user_id = request.values.get("user_id")
		title = request.values.get("title")
		content = request.values.get("content")
		topics_string = request.values.get("topics")

		# The variable `topics` is a list separated by commas. Let's turn ths into list
		topics = topics_string.split(",")

		# Step 2: Perform "form" validation on the provided variables.

		user_from_uid = Users.query.filter_by(id=user_id).first()

		if user_from_uid == None:
			report['msg'] = "The user ID you provided was invalid!"
			report['status'] = False
			return report

		if title == None:
			report['msg'] = "You did not provide a title for your post!"
			report['status'] = False
			return report

		if content == None:
			report['msg'] = "You did not provide any content for your post!"
			report['status'] = False
			return report

		if len(topics) == 0:
			report['msg'] = "You must provide at least one topic for your post!"
			report['status'] = False
			return report


		

		
		# Step 3: If all checks go well, create the post with the `NewPost` class

		new_post_creator = NewPost(user_id, title, content, topics)
		new_post_obj = new_post_creator.create_new_post()

		# Step 4: Create report and return it

		# Step 4a: Check if new_post_obj is invalid.
		
		if new_post_obj == None:
			report['msg'] = "Something went wrong. Please try again."
			report['status'] = False	
			return report

		# Step 4b: Return the report when the creation is succesful.
		
		report['post_id'] = new_post_obj.id
		report['msg'] = "Post created succesfully!"
		report['status'] = True

		return report
	
		
		

api.add_resource(CreatePostResoruce, "/api/post/create")
