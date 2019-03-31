from app import app, api
from flask import request, jsonify
from flask_restful import Resource
from app.rest_api.api_resources.api_decorators import *

from app.models import *
from app.schemas import *

@app.route("/api/groups/all")
@api_require_auth
@api_require_admin
def rest_group_all():
	groups_schema = GroupSchema(many=True)
	all_groups = Group.query.all()
	result_all_grp = groups_schema.dump(all_groups)
	return jsonify(result_all_grp.data)


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
