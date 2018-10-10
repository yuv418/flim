from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Users, Post
from app import app
from app import config
from app.forms import RegistrationForm, LoginForm, NewPostForm, UpdateProfileForm
from app.register import Register
from app.new_post import NewPost
import hashlib


current_config = config.Config()

@app.context_processor
def put_config():
    return dict(config=current_config)

@app.route("/")
@app.route("/index")
def index():
	all_posts = Post.query.all()
	return render_template("index.html", all_posts=all_posts)


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
		
		print(user.password_hashed)
		print(hashlib.sha256(form.password.data.encode('utf-8')).hexdigest())
		flash("Yay! You've succesfully logged in!")
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
	return render_template("user.html", 
		user=user,
		title="User Profile")
		
		
		
@app.route("/new_post", methods=["GET", "POST"])
@login_required
def new_post():
	form = NewPostForm()
	
	print(form.validate_on_submit())
	
	if form.validate_on_submit():
		
		make_new_post = NewPost(current_user.id, form.title.data, form.content.data, form.topics.data)
		new_post = make_new_post.create_new_post()
		
		flash('Post "{}" created succesfully!'.format(str(new_post.title)))
		
		return redirect(url_for('view_post', post_id=new_post.id))
	
	
	return render_template("new_post.html", 
		form=form,
		title="New Post")
		
		
@app.route('/post/<post_id>')
@login_required
def view_post(post_id):
	try:
		post_id = int(post_id)
	except ValueError:
		return "Oops! That's not a valid post!"
	
	post = Post.query.filter_by(id=post_id).first()
	
	if post == None:
		return "Oops! That's not a valid post!"
	
	return render_template("view_post.html",
		post=post, title=post.title)
		
		
@app.route('/update_profile')
def update_profile():
	form = UpdateProfileForm()
	
	return render_template("update_profile.html", form=form)	
	

