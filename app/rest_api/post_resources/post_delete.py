from app import app, api, db
from app.models import *
from app.create.post import NewPost

from flask import request
from flask_restful import Resource

class DeletePostResource(Resource):
	"""
	A resource that allows you to delete a post from the REST API
	Takes parameters:
	    post_id: int
	Returns parameters:
	    status: boolean
	    msg: string
	"""

	def delete(self):

		# Create a report variable to return a report of what has happened.
		report = {}

		# Step 1: retrieve parameters

		post_id = request.values.get("post_id")

		# Step 2: Validate post_id to correspond to a legitimate post. If it does not, then then return a failing report

		post_to_delete = Post.query.filter_by(id=post_id).first()

		if post_to_delete == None:
			report['msg'] = "The post ID that you provided was invalid."
			report['status'] = False
			return report

		# Step 3: Proceed with the deletion. Delete the post.
		
		db.session.delete(post_to_delete)
		db.session.commit()

		# Step 4: Return a successful report.

		report['msg'] = "The post was deleted succesfully."
		report['status'] = True

		return report

api.add_resource(DeletePostResource, "/api/post/delete")
