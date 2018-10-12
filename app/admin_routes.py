from app import app
from flask import render_template

@app.route('/admin/test')
def admin_test():
	return "Test"
