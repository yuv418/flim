from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectMultipleField, widgets
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo
from app.config import Config

current_config = Config()

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
		
	topics = SelectMultipleField("Topics/Tags (Check all that apply)", choices=current_config.app_post_topics_list, option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False))
	
	submit = SubmitField("Post")
	
class UpdateProfileForm(FlaskForm):
	first_name = StringField('First Name')
	last_name = StringField('Last Name')
	
	email = EmailField('Email')
	
	password = PasswordField('Password', validators=[EqualTo('password_validate', message='The passwords must match')])
	password_validate = PasswordField('Password (type again to validate)')
	
	about_me = TextAreaField("About Me")
	
	submit = SubmitField("Update Information")
	
class EditPostForm(FlaskForm):
	content = TextAreaField("New Content")
	
	submit = SubmitField("Update Post")
	
class NewResponseForm(FlaskForm):
	content = TextAreaField("Response")
	submit = SubmitField("Submit Response")
	
class EditResponseForm(FlaskForm):
	content = TextAreaField("Edit Response")
	submit = SubmitField("Update Response")
	
	

	
	
