from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app, config, error_handlers, config_helper, db

from app.forms import *

from app.models import *

from app.create.response import NewResponse
from app.create.subresponse import NewSubResponse

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

