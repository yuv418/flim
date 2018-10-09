from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectMultipleField
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
	
	
class NewPost(FlaskForm):
	title = StringField("Title", validators=[DataRequired()])
	content = TextAreaField("Content", validators=[DataRequired()])
	
	post_topics_list = ["Help Needed", "Idea", "Not Urgent", "Urgent", "Windows", "macOS", "Linux",
		"iOS", "Android", "Windows Phone", "SIM Card Problem", "Phone", "Desktop", "Laptop",
		"Broken", "Data Recovery"]
		
	topics = SelectMultipleField("Topics/Tags", choices=post_topics_list, valdiators[DataRequired()])
	
