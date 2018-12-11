from app import app, api
from flask import request
from flask_restful import Resource

from app.models import * 

class PostByIDResource(Resource):
	def get(self, post_id):
		post = Post.query.filter_by(id=post_id).first()
		return post.as_dict()

class PostByUserIDResource(Resource):
	def get(self, user_id):
		posts = Post.query.filter_by(user_id=user_id).all()
		post_id_list = []
		
		for post in posts:
			post_id_list.append(post.user_id)
		
		return post_id_list
	
class PostByTitleResource(Resource):
	def get(self, title):
		posts = Post.query.filter_by(title=title).all()
		
		post_id_list = []
		
		for post in posts:
			post_id_list.append(post.user_id)
		
		return post_id_list
		
class PostByTimestampResource(Resource):
	def get(self, timestamp):
		posts = Post.query.filter_by(timestamp=timestamp)
		
		post_id_list = []
		
		for post in posts: 
			post_id_list.append(post.user_id)
		
		return post_id_list
		
		
api.add_resource(PostByIDResource, "/api/post/by-id/<post_id>")
api.add_resource(PostByUserIDResource, "/api/post/by-user_id/<user_id>")
api.add_resource(PostByTimestampResource, "/api/post/by-timestamp/<timestamp>")
api.add_resource(PostByTitleResource, "/api/post/by-user_id/<user_id>")
