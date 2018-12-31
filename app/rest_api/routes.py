from flask import request
from flask_restful import Resource
from app import api, app

# Check for a valid api key before the user is allowed to access data.

@app.before_request
def check_apikey_rest_api():
	
	request_paths = request.path.split("/") # looks like ['', 'api', 'blah', 'blah', 'blah'] so we want the first index not the zeroeth index.
	
	if request_paths[1] == "api":
		# An API request
		
		print("API Request!")
	
	# TODO return not found in json format for all api requests.
	
	






from app.rest_api import test
from app.rest_api.user_resources import user_retrieve
from app.rest_api.post_resources import post_retrieve
from app.rest_api.response_resources import response_retrieve
from app.rest_api.group_resources import group_retrieve


