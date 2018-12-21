from app import app, api
from flask import request
from flask_restful import Resource

from app.models import * 

class ResponseByIDResource(Resource):
	def get(self, response_id):
		return Response.query.filter_by(id=response_id).first().as_dict()
	
class ResponseByPostIDResource(Resource):
	def get(self, post_id):
		posts = Response.query.filter_by(post_id=post_id).all()
		posts_id_list = []
		for post in posts:
			posts_id_list.append(post.id)
		
		return posts_id_list

class ResponseByPostIDResource(Resource):
	def get(self, post_id):
		posts = Response.query.filter_by(post_id=post_id).all()
		posts_id_list = []
		for post in posts:
			posts_id_list.append(post.id)
		
		return posts_id_list

class ResponseByUserIDResource(Resource):
	def get(self, user_id):
		posts = Response.query.filter_by(user_id=user_id).all()
		posts_id_list = []
		for post in posts:
			posts_id_list.append(post.id)
		
		return posts_id_list
	
class ResponseByTimestampResource(Resource):
	def get(self, timestamp):
		posts = Response.query.filter_by(timestamp=timestamp).all()
		posts_id_list = []
		for post in posts:
			posts_id_list.append(post.id)
		
		return posts_id_list
	
api.add_resource(ResponseByIDResource, "/api/response/by-id/<response_id>")
api.add_resource(ResponseByPostIDResource, "/api/response/by-post_id/<post_id>")
api.add_resource(ResponseByUserIDResource, "/api/response/by-user_id/<user_id>")
api.add_resource(ResponseByUserIDResource, "/api/response/by-timestamp/<timestamp>")
