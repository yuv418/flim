from app import app, api
from app.models import *
from app.create.group import AddGroup
from app.rest_api.api_resources.api_decorators import *


from flask import request



@app.route("/api/group/create", methods=["POST"])
@api_require("group_name", str)
def rest_add_group():
	# Retrieve variables:
	group_name = request.values.get("group_name")

	# Create Group
	new_group = AddGroup(group_name=group_name)
	new_group_obj = new_group.create()

	# Return successful report
	report = {}
	report['group_id'] = new_group_obj.id
	report['msg'] = "The group was created succesfully"
	report['status'] = True

	return jsonify(report)






#api.add_resource(GroupCreateResource, "/api/group/create")
