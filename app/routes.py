from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app, config, error_handlers, config_helper, db

from app.forms import *
from app.filters import *

from app.admin import routes
from app.rest_api import routes

from app.sp_routes.user_routes import *
from app.sp_routes.post_routes import *
from app.sp_routes.response_routes import *

from app.models import *
from app.schemas import *


from app.update.user_profile import UpdateUserProfile

from app.create.response import NewResponse
from app.create.subresponse import NewSubResponse
from app.create.post import NewPost
from app.create.user import Register


import hashlib


current_config = config.Config()

@app.context_processor
def put_config():
		return dict(config=current_config, config_helper=config_helper)

@app.route("/")
@app.route("/index")
def index():
	all_posts = Post.query.order_by(Post.id.desc()).all()
	return render_template("index.html", all_posts=all_posts)




@app.route("/topic/<topic_name>")
def view_post_topics(topic_name):
	posts = Post.query.all()
	filtered_posts = []


	for post in posts:
		if topic_name in post.get_topics_list(): # if the topic is in the list of topics add to the filtered list
			filtered_posts.append(post)

	return render_template("post_topic_listing.html", topic_name=topic_name, topic_posts=filtered_posts)

@app.route("/fcs")
def fcs():
	return "<title>feature missing</title>Feature coming soon!<br><a href='javascript:window.history.back()'><button>Go back</button></a>"
