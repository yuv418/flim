from app import app, api
from flask import request
from flask_restful import Resource

from app.models import * 

class ResponseByIDResource(Resource):
	def get(self, response_id):
		return Response.query.filter_by(id=response_id).first().as_dict()

class ResponseByPostIDResource(Resource):
	def get(self, post_id):
		responses = Response.query.filter_by(post_id=post_id).all()
		return get_id_list(responses)

class ResponseByPostIDResource(Resource):
	def get(self, post_id):
		posts = Response.query.filter_by(post_id=post_id).all()
		return get_id_list(responses)

class ResponseByUserIDResource(Resource):
	def get(self, user_id):
		posts = Response.query.filter_by(user_id=user_id).all()
		return get_id_list(responses)
	
class ResponseByTimestampResource(Resource):
	def get(self, timestamp):
		posts = Response.query.filter_by(timestamp=timestamp).all()
		return get_id_list(responses)
	
class ResponseByResponseIDResource(Resource):
	def get(self, response_id):
		parent_post = Response.query.filter_by(id=response_id).first()
		posts = parent_post.response_subresponses
		return get_id_list(posts)

api.add_resource(ResponseByIDResource, "/api/response/by-id/<response_id>")
api.add_resource(ResponseByPostIDResource, "/api/response/by-post_id/<post_id>")
api.add_resource(ResponseByUserIDResource, "/api/response/by-user_id/<user_id>")
api.add_resource(ResponseByTimestampResource, "/api/response/by-timestamp/<timestamp>")
api.add_resource(ResponseByResponseIDResource, "/api/response/by-response_id/<response_id>")
