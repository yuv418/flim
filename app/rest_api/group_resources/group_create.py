from app import app, api
from app.models import *
from app.create.group import AddGroup

from flask import request
from flask_restful import Resource


class GroupCreateResource(Resource):
	"""
	Resource to create a group. Admin only.
	Parameters:
	    group_name: str
	Response:
	    status: bool
	    msg: str
	    group_id: int
	"""

	def put(self):
		# Create report variable
		report = {}

		
		# Make sure an admin is creating the group.

		if not Users.get_user_from_api_key(request.values.get('api_key')).is_admin():
			report['msg'] = "You do not have sufficient privileges to perform this task."
			report['status'] = False

			return report
			
		
		
		
		# Step 1: retrieve request variables

		group_name = request.values.get("group_name")

		# Step 2: validate that variables are created

		if not group_name:
			report['msg'] = "The group name you provided was invalid."
			report['status'] = False
			
		# Step 3: Create the group

		new_group = AddGroup(group_name=group_name)

		# Step 4: Create the group and return a successful report.

		new_group_obj = new_group.create()

		
		# Step 5: Return a successful report.

		report['group_id'] = new_group_obj.id
		report['msg'] = "The group was created successfully"
		report['status'] = True

		return report



api.add_resource(GroupCreateResource, "/api/group/create")
		
		
