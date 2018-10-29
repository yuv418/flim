from app import db
from app import app
from app.models import *
from app.forms import NewTopicForm, EditTopicForm

from flask import render_template, abort, request, redirect, flash
from flask_login import current_user, login_manager

from app.admin.instance_stats import InstanceStats

import sys
import json


# ADMIN ROUTES

# All admin route functions are prepended by 'admin_'


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
	
#********************************************** ADMIN HOME **********************************************




#********************************************** END ADMIN HOME **********************************************
	
	
#********************************************** INSTANCE STATS ROUTES **********************************************

istats = InstanceStats()

@app.route('/admin')
@app.route('/admin/stats')
def admin_stats():
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


#********************************************** forum/* ROUTES *************************************************

@app.route('/admin/forum/topics')
def admin_topics_prefs():
	topics = Topic.query.all()
	
	#print(f"DEBUG: topics is {topics}")
	
	return render_template("admin/topics.html", title="Manage Topics", topics=topics)
	
	

@app.route('/admin/forum/topics/new_topic', methods=["GET", "POST"])
def admin_new_topic():
	form = NewTopicForm()
	
	if form.validate_on_submit():
		new_topic = Topic(name=form.topic_name.data)
		db.session.add(new_topic)
		db.session.commit()
		
		flash("Topic added succesfully.")
		
		return redirect(url_for("admin_topics_prefs"))
	
	return render_template("admin/new_topic.html", title="New Topic", form=form)
	
@app.route('/admin/forum/topics/delete_topic/<topic_id>', methods=["GET", "POST"])
def admin_delete_topic(topic_id):
	topic = Topic.query.filter_by(id=topic_id).first()
	
	if topic != None:
		db.session.delete(topic)
		db.session.commit()
		
		flash("Topic removed succesfully.")
		
		return redirect(url_for("admin_topics_prefs"))
		
	flash("Topic removed unsuccesfully.")	
	return redirect(url_for("admin_topics_prefs"))
	
	
@app.route('/admin/forum/topics/edit_topic/<topic_id>', methods=["GET", "POST"])
def admin_edit_topic(topic_id):
	topic = Topic.query.filter_by(id=topic_id).first()
	form = EditTopicForm()
	
	if form.validate_on_submit():
		topic.name = form.new_topic_name.data
		db.session.commit()
		
		flash("Topic updated succesfully.")
		
		return redirect(url_for("admin_topics_prefs"))
	
	form.new_topic_name.default = topic.name
	form.process()
	
	return render_template("admin/edit_topic.html", form=form, title="Edit Topic")


#********************************************** END forum/* ROUTES *********************************************


#********************************************** /admin/user/* ROUTES********************************************

@app.route('/admin/users/signup_settings')
def admin_signup_settings():
	return "Placeholder"


#********************************************** /admin/user/* ROUTES********************************************
