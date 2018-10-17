from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import *
from app import app
from app import config, errors
from app.forms import *
from app.register import Register
from app.new_post import NewPost
from app.update_user_profile import UpdateUserProfile
from app import db
from app.new_response import NewResponse
from app.new_subresponse import NewSubResponse

from app.admin import routes

import hashlib


current_config = config.Config()

@app.context_processor
def put_config():
    return dict(config=current_config)

@app.route("/")
@app.route("/index")
def index():
	all_posts = Post.query.order_by(Post.id.desc()).all()
	return render_template("index.html", all_posts=all_posts)


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
		
		#print(user.password_hashed)
		#print(hashlib.sha256(form.password.data.encode('utf-8')).hexdigest())
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
	posts = Post.query.filter_by(user_id=user.id).all()
	responses = Post.query.filter_by(creator=user).all()
	
	return render_template("user.html", 
		user=user,
		title="User Profile",
		user_posts=posts, 
		user_responses=responses)
		
		
		
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
	
	post_responses = Response.query.filter_by(post_id=post_id).order_by(Response.id.desc()).all()
	filtered_post_responses = []
	for response in post_responses: 
		if not response.is_subresponse(response):
			filtered_post_responses.append(response)			
		
			
	
	
	post = Post.query.filter_by(id=post_id).first()
	
	
	if post == None:
		return "Oops! That's not a valid post!"
	
	return render_template("view_post.html",
		post=post, title=post.title, post_responses=filtered_post_responses, post_responses_len=len(post_responses))
		
		
@app.route('/update_profile', methods=["GET", "POST"])
@login_required
def update_profile():
	form = UpdateProfileForm()
	
	if form.validate_on_submit():
		
		u = UpdateUserProfile(form.first_name.data, form.last_name.data, form.email.data, form.password.data, form.password_validate.data, form.about_me.data, current_user)
		u.update()
		
		flash("Updated profile succesfully.")
		return redirect(url_for("user_profile", name=current_user.username))
		
	return render_template("update_profile.html", form=form)
	
@app.route('/edit_post/<post_id>', methods=["GET", "POST"])
@login_required
def edit_post(post_id):
	post = Post.query.filter_by(id=post_id).first()
	form = EditPostForm()
	
	if form.validate_on_submit():
		post.content = form.content.data
		post.topics = json.dumps(form.topics.data)
		
		db.session.commit()
		
		flash("Post edited succesfully!")
		return redirect(url_for("view_post", post_id=post.id))
		
	if not post.creator == current_user:
		flash("You must be logged in as the creator of this post in order to edit it.")
		return redirect(url_for("view_post", post_id=post.id))
	
	form.content.default = post.content	
	
	default_topics = []
	
	for topic in post.get_topics_list():
		default_topics.append(topic)
	
	form.topics.default = default_topics
	form.process()
	

	
	return render_template("edit_post.html", form=form)
	
@app.route('/delete_post/<post_id>', methods=["GET", "POST"])
def delete_post(post_id):
	post = Post.query.filter_by(id=post_id).first()
	
	if not current_user == post.creator:
		flash("You do not have the correct permissions to perform this action.")
		return redirect(url_for('view_post', post_id=post.id))
	
	
	db.session.delete(post)
	db.session.commit()
	
	flash("Post succesfully deleted!")
	
	return redirect(url_for("index"))

@app.route('/new_response/<post_id>', methods=["GET", "POST"])
@login_required
def new_response(post_id):
	post = Post.query.filter_by(id=post_id).first()
	
	form = NewResponseForm()
	
	if form.validate_on_submit():
		new_response = NewResponse(current_user, post, form.content.data)
		new_response.add_response()
		
		flash("Response added succesfully!")
		return redirect(url_for("view_post", post_id=post.id))
	
	return render_template("new_response.html", form=form, post=post)

	
@app.route("/edit_response/<response_id>", methods=["GET", "POST"])
@login_required
def edit_response(response_id):
	response = Response.query.filter_by(id=response_id).first()
	
	form = EditResponseForm()
		
	if form.validate_on_submit():
		
		response.content = form.content.data
		db.session.commit()
		
		return redirect(url_for("view_post", post_id=response.post_id))
		
	form.content.default = response.content
	form.process()
	
	return render_template("edit_response.html", form=form)
	
	
@app.route('/delete_response/<response_id>')
@login_required
def delete_response(response_id):
	response = Response.query.filter_by(id=response_id).first()
	
	response_post_id = response.parent_post.id
	if not response.creator == current_user:
		flash("You do not have the correct permissions to do this.")
		return redirect(url_for("view_post", post_id=response_post_id))
	
	db.session.delete(response)
	db.session.commit()
	
	
	
	flash("Post deleted succesfully.")
	return redirect(url_for("view_post", post_id=response_post_id))

@app.route("/topic/<topic_name>")
def view_post_topics(topic_name):
	posts = Post.query.all()
	filtered_posts = []
	
	
	for post in posts:
		if topic_name in post.get_topics_list(): # if the topic is in the list of topics add to the filtered list
			filtered_posts.append(post)
		
	return render_template("post_topic_listing.html", topic_name=topic_name, topic_posts=filtered_posts)

@app.route("/new_subresponse/<parent_response_id>", methods=["GET", "POST"])
@login_required
def new_subresponse(parent_response_id):
	form = NewResponseForm()
	response = Response.query.filter_by(id=parent_response_id).first()
	post = Post.query.filter_by(id=response.parent_post.id).first()
	
	if form.validate_on_submit():
		nrsp = NewSubResponse(form.content.data, response, current_user)
		nrsp.create_subpresponse()
		
		flash("Subresponse added sucessfully!")
		return redirect(url_for("view_post", post_id=response.parent_post.id))
	
	
	return render_template("new_response.html", form=form, post=post, subresponse=True)
