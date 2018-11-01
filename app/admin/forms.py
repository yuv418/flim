from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField

from app.models import DBConfig


class SignUpPermissionsForm(FlaskForm):
	allow_registration = BooleanField('Allow registration', default=bool(DBConfig.get_value("app_allow_registration")))
	submit = SubmitField("Update")
	
	
class NewTopicForm(FlaskForm):
	topic_name = StringField("Topic Name: ")
	submit = SubmitField("Create")
	
class EditTopicForm(FlaskForm):
	new_topic_name = StringField("New Topic Name: ")
	submit = SubmitField("Update")
