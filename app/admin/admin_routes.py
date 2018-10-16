from app import app
from flask import render_template
import sys 

@app.route('/admin/version')
def admin_test():
	return render_template("admin/version.html", sys=sys)

