from app import app
from flask import render_template, abort, request
import sys 


@app.before_request
def restrict_admin_access():
	request_paths = request.path.split('/')
	


@app.route('/admin/version')
def admin_test():
	return render_template("admin/version.html", sys=sys)

