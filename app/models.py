from app import db
from app import login
from flask import url_for
from flask_login import UserMixin
from datetime import datetime
from app.config import Config
import hashlib
import json

currentconfig = Config()

class Users(UserMixin, db.Model):
	__tablename__='users'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(128), index=True, unique=True)
	last_name = db.Column(db.String(128), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	about = db.Column(db.Text(512), index=True, unique=True) 
	password_hashed = db.Column(db.String(255), index=True, unique=True)
	username = db.Column(db.String(32), index=True, unique=True)
	
	post = db.relationship('Post', backref='creator')
	response = db.relationship('Response', backref='creator')
	
	def set_password(self, password):
		self.password_hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
	
	def check_password(self, check_password):
		return self.password_hashed ==  hashlib.sha256(check_password.encode('utf-8')).hexdigest()
		
	@login.user_loader
	def load_user(id):
		return Users.query.get(int(id))
	
	def __repr__(self): 
		return "<object User {}>".format(self.username)

class Post(db.Model):
	__tablename__ = "post"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
	
	title = db.Column(db.String(128), index=True) 
	content = db.Column(db.Text(9990), index=True)
	
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) 
	
	topics = db.Column(db.Text(9999), index=True, default="")	
	
	response = db.relationship("Response", backref="parent_post")
	
	def get_topics_list(self):
		return json.loads(self.topics)
	

	def __repr__(self):
		return "<object Post {} {}>".format(self.id, self.title)
		
class Response(db.Model):
	__tablename__ = "responses"
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	
	post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
	
	content = db.Column(db.Text(9990))
	
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	
	def __repr__(self):
		return "<object Response post_id:{}>".format(post_id)
