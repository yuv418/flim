# User routes for flim

from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app, config, error_handlers, config_helper, db

from app.forms import *
from app.models import *

from app.update.user_profile import UpdateUserProfile

from app.create.user import Register

import hashlib

current_config = config.Config()

@app.route('/register', methods=['GET', 'POST'])
def register():
	if not current_config.app_allow_registration:
		flash("Registration is disallowed right now.")
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():

		register = Register(form.first_name.data,
			form.last_name.data,
			form.email.data,
			form.password.data,
			form.username.data)

		register.register()

		flash('User registered successfully.')

		return redirect('/index')

	return render_template("register.html",
		form=form,
		title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = Users.query.filter_by(username=form.username.data).first() # get the user

		if user is None or not user.check_password(form.password.data):
			flash("Oops! Please try again.")
			return redirect(url_for('login'))


		flash("You've succesfully logged in.")
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index')) # this will be changed to user profile page TODO

	return render_template("login.html",
		form=form,
		title="Login")

@app.route("/logout")
def logout():
	logout_user()
	flash("You have succesfully been logged out.")
	return redirect(url_for("index"))


@app.route("/user/<name>")
@login_required
def user_profile(name):
	user = Users.query.filter_by(username=name).first_or_404()
	posts = Post.query.filter_by(user_id=user.id).all()
	responses = Response.query.filter_by(creator=user).all()

	return render_template("user.html",
		user=user,
		title="User Profile",
		user_posts=posts,
		user_responses=responses)
