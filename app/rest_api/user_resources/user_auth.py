from flask import request, jsonify
from app import app
from app.rest_api.api_resources.api_decorators import *

from app.models import *

@app.route("/api/user/auth", methods=["POST"])
@api_require("username", str)
@api_require("password", str)
def check_user_auth():
	report = {}

	# Get request params
	username = request.values.get("username")
	password = request.values.get("password")

	# Find user
	user = Users.query.filter_by(username=username).first()

	# Check password
	pw_chk = user.check_password(password)

	# Return password check

	return jsonify({"status": pw_chk})

