from app import app
from app.models import *

from flask import render_template, abort, request
from flask_login import current_user

import sys 


@app.before_request
def restrict_admin_access():
	request_paths = request.path.split('/')
	admin_group = Group.admin_group()
	
	if request_paths[0] == "admin":
		if not admin_group in current_user.groups: # not an admin
			response.status = 403
			return response
			
	
	


@app.route('/admin/version')
def admin_test():
	return render_template("admin/version.html", sys=sys)

