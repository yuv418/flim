from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import InputRequired, DataRequired

from app.models import DBConfig


class SignUpPermissionsForm(FlaskForm):
	allow_registration = BooleanField('Allow registration', default=bool(DBConfig.get_value("app_allow_registration")))
	submit = SubmitField("Update")
	
	
class NewTopicForm(FlaskForm):
	topic_name = StringField("Topic Name: ", validators=[InputRequired()])
	submit = SubmitField("Create")
	
class EditTopicForm(FlaskForm):
	new_topic_name = StringField("New Topic Name: ", validators=[InputRequired()])
	submit = SubmitField("Update")
	
class CreateGroupForm(FlaskForm):
	group_name = StringField("Group Name:", validators=[InputRequired()])
	submit = SubmitField("Create")
	

