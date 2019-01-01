from app.models import Users
from app import db
import hashlib 

class Register:
	def __init__(self, first_name, last_name, email, password, username):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
		self.username = username
	
	def register(self):
		new_user = Users(first_name=self.first_name,
			last_name=self.last_name,
			email=self.email,
			password_hashed=self.hashed_password,
			username=self.username)
		db.session.add(new_user)
		db.session.commit()
		
		


