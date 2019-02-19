from flask import request, jsonify
from functools import wraps
from flask_login import current_user

from app.models import Users
from app.rest_api.models import APIKey
import traceback
def api_check_auth(f):
	@wraps(f)
	def dec_fn(*args, **kwargs):
		"""Check authorization for users that are utilizing the REST API."""
		# There are 3 ways to log in as of today: API Key, or be logged in in the session.

		# Retrieve the API key first.

		api_key_param = request.values.get("api_key")
		api_key = APIKey.query.filter_by(api_key=api_key_param).first()

		if current_user.is_anonymous and api_key == None:
			# The user is not logged in and no API key was provided
			return jsonify({"status": False, "msg": "You are unauthorized to access this resource."}), 403
		else:
			return f(*args, **kwargs)

		# The API key must correspond to a valid user, get the user from the API key.

		api_user = Users.get_user_from_api_key(api_key_param)
		print(f"API user is {api_user}")

		# Make sure the API user is not invalid, otherwise continue

		if  api_user == None:
			return jsonify({"status": False, "msg": "You are unauthorized to access this resource."}), 403

		return f(*args, **kwargs)

	return dec_fn

def api_require(param_name, param_type):
	"""Decorator will check if param_name is param_type or if param_name is included, otherwise decorator will return error 400 with status = False"""
	def dec(f):
		@wraps(f)
		def dec_fn(*args, **kwargs):
			if request.values.get(param_name) != None:
				try:
					# Try to turn param_name into param_type
					cast = param_type(request.values.get(param_name))
					return f(*args, **kwargs)
				except ValueError:
					traceback.print_exc()
					return jsonify({"status": False, "msg": f"Parameter '{param_name}' is invalid"}), 400

			return jsonify({"status": False, "msg": f"Parameter '{param_name}' is invalid"}), 400
		return dec_fn
	return dec
