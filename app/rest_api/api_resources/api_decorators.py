from flask import request, jsonify
from functools import wraps
from flask_login import current_user

from app.models import Users
from app.rest_api.models import APIKey
import traceback
def api_require_auth(f):
	@wraps(f)
	def dec_fn(*args, **kwargs):
		"""Check authorization for users that are utilizing the REST API."""
		# There are 3 ways to log in as of today: API Key, be logged in in the session, or provide a username and password.


		# Retrieve the API key.

		api_key_param = request.values.get("api_key")
		api_key = APIKey.query.filter_by(api_key=api_key_param).first()

		# Retrieve the user and password and attempt to create a user.

		username = request.values.get("auth_username")
		password = request.values.get("auth_password")

		user = Users.query.filter_by(username=username).first()

		if current_user.is_anonymous and api_key == None and user == None:
			# The user is not logged in and no API key was provided and no user credentials were provided
			return jsonify({"status": False, "msg": "You are unauthorized to access this resource."}), 403

		elif not current_user.is_anonymous:
			return f(*args, **kwargs)

		elif api_key != None:
			# API key provided, make sure a corresponding user exists.

			api_user = Users.get_user_from_api_key(api_key_param)
			print(f"API user is {api_user}")

			# Make sure the API user is not invalid, otherwise continue

			if  api_user == None:
				return jsonify({"status": False, "msg": "You are unauthorized to access this resource."}), 403
			else:
				return f(*args, **kwargs)
		elif user != None:
			# User might exist, check their password
			if user.check_password(password):
				return f(*args, *kwargs)
			else:
				return jsonify({"status": False, "msg": "You are unauthorized to access this resource."}), 403


		return f(*args, **kwargs)

		# The API key must correspond to a valid user, get the user from the API key.


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




def api_require_admin(f):
	@wraps(f)
	def dec_fn(*args, **kwargs):
		"""Function to require a user to be an administrator when they do something on the REST API"""

		# Get the API user

		api_user = get_api_user(request.values)

		# Prevent non-admins or invalid users from accessing resources

		if api_user == None or not api_user.is_admin():
			return jsonify({"status": False, "msg": "You are unauthorized to access this resource."}), 403
		elif api_user.is_admin():
			return f(*args, **kwargs)

	return dec_fn




def get_api_user(request_values):
	"""Function to return the user that used the API"""

	username = request_values.get('auth_username')
	password = request_values.get('auth_password')
	api_key = request_values.get('api_key')
	# Check username and password auth

	if username and password:
		# User requested user authentication
		api_user = Users.query.filter_by(username=username).first()
		# Make sure password is valid
		if api_user.check_password(password):
			return api_user
		else:
			return None

	# Check API Key auth

	if api_key:
		api_user = Users.get_user_from_api_key(api_key)
		if api_user is not None:
			return api_user
		else:
			return None


