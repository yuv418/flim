from app import app, api
from flask import request
from flask_restful import Resource

from app.models import *

class UserResource(Resource):
	def get(self, user_id):
		user = Users.query.filter_by(id=user_id).first()
		return user.as_dict()
		
class GroupResource(Resource):
	def get(self, group_id):
		group = Group.query.filter_by(id=group_id).first()
		return group.as_dict()
		
class PostResource(Resource):
	def get(self, post_id):
		post = Post.query.filter_by(id=post_id).first()
		return post.as_dict()
		
		
class ResponseResource(Resource):
	def get(self, response_id):
		response = Response.query.filter_by(id=response_id).first()
		return response.as_dict()
		
class TopicResource(Resource):
	def get(self, topic_name):
		
		ndict = {}
		posts_relating = []
		posts_list = Post.query.all()
		
		for post in posts_list:
			topics_list = post.get_topics_list()
			if topic_name in topics_list:
				posts_relating.append(post.id)
	
		ndict['posts'] = posts_relating
		
		return ndict
	

				
				
		
api.add_resource(UserResource, "/api/user/<user_id>")
api.add_resource(GroupResource, "/api/group/<group_id>")
api.add_resource(PostResource, "/api/post/<post_id>")
api.add_resource(ResponseResource, "/api/response/<response_id>")
api.add_resource(TopicResource, "/api/topic/<topic_name>")
		
		
	
