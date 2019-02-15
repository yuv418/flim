from flask import request, jsonify
from functools import wraps
from flask_login import current_user

from app.models import Users

def api_check_auth(f):
	@wraps(f)
	def dec_fn(*args, **kwargs):
		"""Check authorization for users that are utilizing the REST API."""


		
		
		# There are 3 ways to log in as of today: API Key, or be logged in in the session.

		# Retrieve the API key first.
		
		api_key = request.values.get("api_key")

		
		if current_user.is_anonymous and api_key is None:
			# The user is not logged in
			return jsonify({"status": False, "msg": "You are unauthorized to access this resource."}), 403
		else:
			return f(*args, **kwargs)
	


		# The API key must correspond to a valid user, get the user from the API key.

		api_user = Users.get_user_from_api_key(api_key)
		print(api_user)


		# Make sure the API user is not invalid, otherwise continue
		
		if  api_user == None: 
			return jsonify({"status": False, "msg": "You are unauthorized to access this resource."}), 403
		

	


	

	

	
	
	


	
		
						   
		return f(*args, **kwargs)
	return dec_fn
		
