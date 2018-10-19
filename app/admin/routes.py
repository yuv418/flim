from app import app
from app.models import *

from flask import render_template, abort, request
from flask_login import current_user, login_manager

from app.admin.instance_stats import InstanceStats

import sys
import json


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
	
	
#********************************************** INSTANCE STATS **********************************************

istats = InstanceStats()

@app.route('/admin/stats')
def stats():
	return render_template('admin/stats.html', istats=istats, title="Stats")
	
@app.route('/admin/stats/cpuload_percent')
def cpuload_percent():
	return json.dumps(istats.cpu_load_percent())
	
@app.route('/admin/stats/cpuload_freq')
def cpuload_freq():
	return json.dumps(istats.cpu_current_frequencies())
	
@app.route('/admin/stats/avail_mem')
def avail_mem():
	print(round(istats.available_mem(), 2))
	return str(round(istats.available_mem(), 2))
	
@app.route('/admin/stats/avail_swap_mem')
def avail_swap_mem():
	print(round(istats.available_swap_mem(), 2))
	return str(round(istats.available_swap_mem(), 2))
	
	
	
	
#********************************************** END INSTANCE STATS **********************************************