from app import app, api
from flask_restful import reqparse, Resource

class GroupUpdateResource(Resource):
	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument("id", type=int, help="Please provide a valid group id")
		parser.add_argument("name", type=str, help="Please provide a valid name")
