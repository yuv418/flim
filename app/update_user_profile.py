from app import db
from app.models import Users
import hashlib 

class UpdateUserProfile:
	def __init__(self, first_name, last_name, email, password, password_validate, about_me, user):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = hashlib.sha256(password.encode("utf-8")).hexdigest()
		self.password_validate = hashlib.sha256(password_validate.encode("utf-8")).hexdigest()
		self.about_me = about_me
		self.user = user
	
	def update(self):
		status = True
		
		if not self.first_name == "":
			self.user.first_name = self.first_name
		else:
			status = False
		
		if not self.last_name == "":
			self.user.last_name = self.last_name
		else: 
			status = False
		
		if not self.email == "":
			self.user.email = self.email
		else: 
			status = False
		
		if not self.password == "":
			if self.password_validate == self.password:
				self.user.password_hashed = self.password
		
		if not self.about_me == "":
			self.user.about = self.about_me
			
		db.session.commit()
		
	
