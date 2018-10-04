from flask import render_template, flash, redirect
from app import app
from app import config
from app.forms import RegistrationForm


current_config = config.Config()


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html", config=current_config)


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		
		flash('Registration requested for user {}, first_name {} and last_name {}'.format( 
			form.username.data, form.first_name.data, form.last_name.data))
		
		return redirect('/index')
	return render_template("register.html", 
		config=current_config, 
		form=form,
		title="Register")
		

