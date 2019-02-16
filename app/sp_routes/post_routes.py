from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app, config, error_handlers, config_helper, db

from app.forms import *


from app.models import *
from app.schemas import *

from app.create.post import NewPost


@app.route("/new_post", methods=["GET", "POST"])
@login_required
def new_post():
	form = NewPostForm()



	if validate_newpost_form(form):


		stripped_topics_data = [data.strip() for data in form.topics.data]

		make_new_post = NewPost(current_user.id, form.title.data.strip(), form.content.data, stripped_topics_data)
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


