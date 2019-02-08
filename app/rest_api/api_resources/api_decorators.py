from flask import request, jsonify
from functools import wraps
from flask_login import current_user

def api_check_auth(f):
	@wraps(f)
	def dec_fn(*args, **kwargs):
		"""Check authorization for users that are utilizing the REST API."""

		# There are 3 ways to log in as of today: HTTP Basic, API Key, or part of the session.
		if current_user.is_anonymous:
			# The user is not logged in
			return jsonify({"status": False, "msg": "You are unauthorized to access this resource."}), 403

		
		

						   
		return f(*args, **kwargs)
	return dec_fn
		
