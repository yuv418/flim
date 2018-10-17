from app import app
from app.models import *

from flask import render_template, abort, request
from flask_login import current_user, login_manager

import sys 


@app.before_request
def restrict_admin_access():
	
	request_paths = request.path.split('/')
	admin_group = Group.admin_group()
	
	if request_paths[1] == "admin":
		if not admin_group in current_user.groups: # not an admin
			return 'Permission Denied', 403 
	
	


@app.route('/admin/version')
def admin_test():
	return render_template("admin/version.html", sys=sys, title="Version")

