from flask import request
from flask_restful import Resource
from app import api


class Test(Resource):
	def get(self):
		return {"status": True, "msg": "test"}



api.add_resource(Test, "/api/test")
