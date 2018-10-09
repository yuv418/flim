from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Users
from app import app
from app import config
from app.forms import RegistrationForm, LoginForm, NewPostForm
from app.register import Register
import hashlib

current_config = config.Config()


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html", config=current_config)


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		
		
			
		register = Register(form.first_name.data,
			form.last_name.data,
			form.email.data,
			form.password.data,
			form.username.data)
			
		register.register()
		
		flash('Registration requested for user!')
		
		return redirect('/index')
	return render_template("register.html", 
		config=current_config, 
		form=form,
		title="Register")
		

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	
	if form.validate_on_submit():
		user = Users.query.filter_by(username=form.username.data).first() # get the user
		print(user.password_hashed)
		print(hashlib.sha256(form.password.data.encode('utf-8')).hexdigest())
		if user is None or not user.check_password(form.password.data):
			flash("Oops! Please try again.")
			return redirect(url_for('login'))
		flash("Yay! You've succesfully logged in!")
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index')) # this will be changed to user profile page TODO
	
	return render_template("login.html",
		config=current_config,
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
	return render_template("user.html", 
		config=current_config,
		user=user,
		title="User Profile")
		
		
		
@app.route("/new_post")
@login_required
def new_post():
	
	form = NewPostForm()
	
	return render_template("new_post.html", 
		config=current_config,
		form=form
		title="New Post")
		
	

