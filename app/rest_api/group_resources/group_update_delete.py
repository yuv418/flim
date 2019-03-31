from app import app, api, db
from flask import request, jsonify
from app.rest_api.api_resources.api_decorators import *
from app.models import *

@app.route("/api/group/<int:id>", methods=["PUT"])
@api_require("name", str)
def api_update_group(id):
	group = Group.query.filter_by(id=id).first()
	group.name = request.values.get("name")

	db.session.commit()

	return jsonify({"status": True, "msg": "Group updated successfully"})

@app.route("/api/group/<int:id>", methods=["DELETE"])
def api_delete_group(id):
	group = Group.query.filter_by(id=id).first()

	db.session.delete(group)
	db.session.commit()

	return jsonify({"status": True, "msg": f"Group '{group.name}' deleted successfully"})
