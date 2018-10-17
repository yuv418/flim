from app import app
from flask import render_template, abort, request
from flask_login import current_user
import sys 


@app.before_request
def restrict_admin_access():
	request_paths = request.path.split('/')
	if request_paths[0] == "admin":
		if not current_user.is_admin:
			response.status = 403
			return response
			
	
	


@app.route('/admin/version')
def admin_test():
	return render_template("admin/version.html", sys=sys)

