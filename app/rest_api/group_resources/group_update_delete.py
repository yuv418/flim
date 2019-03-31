from app import app, api, db
from flask import request, jsonify
from app.rest_api.api_resources.api_decorators import *
from app.models import *

@app.route("/api/group", methods=["PUT"])
@api_require_auth
@api_require_admin
@api_require('id', int)
@api_require("name", str)
def api_update_group():


	group = Group.query.filter_by(id=request.values.get('id')).first()
	if not group:
		return jsonify({"status": False, "msg": "Group doesn't exist!"})
	group.name = request.values.get("name")

	db.session.commit()

	return jsonify({"status": True, "msg": "Group updated successfully"})

@app.route("/api/group", methods=["DELETE"])
@api_require_auth
@api_require_admin
@api_require('id', int)
def api_delete_group():

	group = Group.query.filter_by(id=request.values.get('id')).first()

	db.session.delete(group)
	db.session.commit()

	return jsonify({"status": True, "msg": f"Group '{group.name}' deleted successfully"})
