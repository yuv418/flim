from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectMultipleField, widgets
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	username = StringField('Username', validators=[DataRequired()])
	email = EmailField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_validate', message='The passwords must match')])
	password_validate = PasswordField('Password (type again to validate)', validators=[DataRequired()])
	submit = SubmitField('Register')
	
class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	remember_me = BooleanField("Remember", validators=[DataRequired()])
	submit = SubmitField("Log In")
	
	
class NewPostForm(FlaskForm):
	title = StringField("Title", validators=[DataRequired()])
	content = TextAreaField("Content", validators=[DataRequired()])
	
	post_topics_list = [("Help Needed", "Help Needed"), ("Idea", "Idea"), ("Not Urgent", "Not Urgent"), ("Urgent", "Urgent"), ("Windows", "Windows"), ("macOS", "macOS"), ("Linux", "Linux"),
		("iOS", "iOS"), ("Android", "Android"), ("Windows Phone", "Windows Phone"), ("SIM Card Problem", "SIM Card Problem"), ("Phone", "Phone"), ("Desktop", "Desktop"), ("Laptop", "Laptop"),
		("Broken", "Broken"), ("Data Recovery", "Data Recovery")] 
		
		#TODO make this part of the db and dynamic
		
	topics = SelectMultipleField("Topics/Tags (Check all that apply)", choices=post_topics_list, option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False), validators=[DataRequired()])
	
	submit = SubmitField("Post")
	
class UpdateProfileForm(FlaskForm):
	first_name = StringField('First Name')
	last_name = StringField('Last Name')
	
	email = EmailField('Email')
	
	password = PasswordField('Password', validators=[EqualTo('password_validate', message='The passwords must match')])
	password_validate = PasswordField('Password (type again to validate)')
	
	about_me = TextAreaField("About Me: ")
	
	submit = SubmitField("Update Information")
	
	

	
	
