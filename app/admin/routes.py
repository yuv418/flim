from app import app
from flask import render_template, abort, request
import sys 


@app.before_request



@app.route('/admin/version')
def admin_test():
	return render_template("admin/version.html", sys=sys)

