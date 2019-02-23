from app import app, api
from flask import request
from flask_restful import Resource

from app.models import * 

@app.route("/api/group/all")
def rest_group_all():
	pass


class GroupByIDResource(Resource):
	def get(self, group_id):
		group = Group.query.filter_by(id=group_id).first()
		return group.as_dict()

class GroupByNameResource(Resource):
	def get(self, group_name):
		groups = Group.query.filter_by(name=group_name).all()
		return get_id_list(groups)

class GroupAllResource(Resource):
	def get(self):
		groups = Group.query.all()
		return get_id_list(groups)

api.add_resource(GroupByIDResource, "/api/group/by-id/<group_id>")
api.add_resource(GroupByNameResource, "/api/group/by-name/<group_name>")
#api.add_resource(GroupAllResource, "/api/group/all")
