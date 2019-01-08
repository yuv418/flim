from app import app, api, db
from app.models import *
from app.create.post import NewPost

from flask import request
from flask_restful import Resource

class UpdatePostResource(Resource):
	"""
	A resource that allows you to delete a post from the REST API
	Takes parameters:
	    post_id: int
	    (the following parameters are optional, this resource takes at least one:)
	    title: string
	    content: string
	    topics: list (comma-separated values in string)

	Returns parameters:
	    status: boolean
	    msg: string
	"""

	def put(self):

		# Step 1: create the report dictionary

		report = {}

		# Step 2: retrieve variables from request.

		post_id = request.values.get("post_id")
		new_title = request.values.get("title")
		new_content = request.values.get("content")
		new_topics_string = request.values.get("topics")
		new_topics = new_topics_string.split(",")
		
		# Step 3: Check if the post_id does not correspond to a post.

		post_to_update = Post.query.filter_by(id=post_id).first()

		if post_to_update == None:
			report['msg'] = "The post ID you provided was invalid."
			report['status'] = False
			return report

			
		# Step 4: Check which values need to be updated and update the post with the new values.
		
		if new_topics != None:
			post_to_update.topics = new_topics

		if new_title != None:
			post_to_update.title = new_title

		if new_content != None:
			post_to_update.content = content

		# Update the post with the new values

		db.session.commit()

		# Step 5: return successful report.

		report['msg'] = "The post was updated succesfully."
		report['status'] = True

		return report

api.add_resource(UpdatePostResource, "/api/post/update")
			
			
		
