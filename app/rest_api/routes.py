from flask import request, jsonify
from flask_restful import Resource
from app import api, app
from app.rest_api.models import *

# Check for a valid api key before the user is allowed to access data.




from app.rest_api.api_resources import api_manage
from app.rest_api import test
from app.rest_api.user_resources import user_create
from app.rest_api.user_resources import user_retrieve
from app.rest_api.user_resources import user_update
from app.rest_api.user_resources import user_delete
from app.rest_api.user_resources import user_auth
from app.rest_api.post_resources import post_retrieve
from app.rest_api.response_resources import response_retrieve
from app.rest_api.response_resources import response_create
from app.rest_api.group_resources import group_retrieve
from app.rest_api.group_resources import group_create
from app.rest_api.group_resources import group_update_delete
from app.rest_api.post_resources import post_create
from app.rest_api.post_resources import post_delete
from app.rest_api.post_resources import post_update


