from app import db
from app.config import Config

# Needed for generating API keys

import string
import random

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
	
	user = db.relationship("Users", back_populates="api_keys")
	
	
	# We also want to store the API key. Index this for faster results. Finally, we also need a description for the API keys. This is optional.
	
	api_key = db.Column(db.String(256), index=True)
	
	description = db.Column(db.Text(current_config.app_message_max_length))
	
	
	# We want to implement the standard function as_json to get the class represented as a dictionary.
	
	def as_dict(self):
		"""
		Function that returns a representation of the APIKey class as a dictionary which can easily be turned into JSON.
		"""
		
		# Create a new dictionary called ndict to store attributes about the object
		
		ndict = {}
		
		# Populate the dictionary. We omit 'user' because it is better for there to be less information in each request and we want to follow the standard format of all as_dict functions.
		
		ndict['id'] = self.id
		ndict['user_id'] = self.user_id
		ndict['api_key'] = self.api_key
		ndict['description'] = self.description
		
		return ndict
	
	
	# Function create_api_key(user, description) 
	
	@staticmethod
	def create_api_key(user, description=""):
		"""
		This function creates and adds an API key to the database when a user (type Users) is given. The description is optional, it needs to be of type 'str'. The user is given a random API key. 
		This function returns a variable api_key of type 'str'.
		"""
		
		# The way we are going to create a random API key is go through a pool of 62 characters (string.ascii_letters and string.digits) and choose a letter randomly 100 times.
		
		letters = string.ascii_letters + string.digits
		new_api_key = ""
		
		# Loop through and add to the new_api_key while removing from the letters.
		
		for i in range(100):
			
			# Step 1: Choose a letter
			
			letter_choice = random.choice(letters)
			
			# Step 2: Add to the API key
			
			new_api_key += letter_choice
			
			
		# Our new API key is now ready. Now we will add it to the table.
		
		new_api_key_entry = APIKey(user=user, api_key=new_api_key, description=description)
		
		db.session.add(new_api_key_entry)
		db.session.commit()
		
			
		# Return the API key at the end.
			
		return new_api_key
			
		
	
		
	

	
