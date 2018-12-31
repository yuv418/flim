from app import db
from app.config import Config

current_config = Config()

class APIKey(db.Model):
	"""
	Database model that links a user to an API key. This is a one-to-many relationship, a user will get one API key EACH. 
	The number of API keys can be configured in config.py under the variable app_rest_api_key_limit.
	"""

	__tablename__ = "api_keys"
	
	# As always, everything has an ID.
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	
	
	# This defines to use that there is a column called users.id that links back to the users table to get the user_id
	
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
	
	
	# The model should also be easy to use, so we define the user itself so the programmer does not have to retrieve the user manually.
	
	user = db.relationship("User", back_populates="api_keys")
	

	
