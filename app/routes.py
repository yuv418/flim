from flask import render_template, flash, redirect
from app import app
from app import config
from app.forms import RegistrationForm
from app.register import Register

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
		

