from flask import request, jsonify
from flask_restful import Resource
from app import api, app
from app.rest_api.models import *

# Check for a valid api key before the user is allowed to access data.

@app.before_request
def check_apikey_rest_api():
	
	request_paths = request.path.split("/") # looks like ['', 'api', 'blah', 'blah', 'blah'] so we want the first index not the zeroeth index.
	
	
	if request_paths[1] == "api" and request_paths[2] + "/" + request_paths[3] != 'key/add':
		# An API request (unless we are trying to add a key)
		
		
		# We must check if the request contains an API key. The API key is sent as api_key.
		
		api_key = request.values.get("api_key")
		
		if api_key == None:
			
			# The user has not even specified an API key.
			
			report = {}
			report['msg'] = "Access denied. You have not provided an API key!"
			
			# Return this report
			
			return jsonify(report)
			
		else: 
			
			# The user has provided an API key. We must check if the API key is valid. We do this by querying the database to see if there is a column that lists the API key.
			
			api_key_entry = APIKey.query.filter_by(api_key=api_key).first()
			
			if api_key_entry == None:
				
				# The user does not have access to the API. Their API key is invalid.
				
				report = {}
				report['msg'] = "Access denied. Your API key is invalid!"
					
				return jsonify(report)
					
			
				
		# The user does have access to the API. The function may return empty for everything to proceed.

	
	

from app.rest_api.api_resources import api_manage

from app.rest_api.user_resources import user_retrieve
from app.rest_api.user_resources import user_update
from app.rest_api.post_resources import post_retrieve
from app.rest_api.response_resources import response_retrieve
from app.rest_api.response_resources import response_create
from app.rest_api.group_resources import group_retrieve
from app.rest_api.group_resources import group_create
from app.rest_api.post_resources import post_create
from app.rest_api.post_resources import post_delete
from app.rest_api.post_resources import post_update


