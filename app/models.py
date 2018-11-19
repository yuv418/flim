from app import db
from app import login
from flask import url_for
from flask_login import UserMixin
from datetime import datetime
from app.config import Config
import hashlib
import json

current_config = Config()

subresponses = db.Table('subresponses', 
	db.Column('response_id', db.Integer, db.ForeignKey('responses.id')),
	db.Column('subresponse_id', db.Integer, db.ForeignKey('responses.id'))
)

group_associations = db.Table('group_associations',
	db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
	db.Column('group_id', db.Integer, db.ForeignKey('groups.id'))
)

class Topic(db.Model):
	__tablename__ = 'topics'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(512), index=True)
	
		
	
	def __repr__(self):
		return f"<Topic {self.name}>"

class Users(UserMixin, db.Model):
	__tablename__='users'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(128), index=True, unique=True)
	last_name = db.Column(db.String(128), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	about = db.Column(db.Text(9990), index=True, unique=True) 
	password_hashed = db.Column(db.String(255), index=True, unique=True)
	username = db.Column(db.String(32), index=True, unique=True)
	
	post = db.relationship('Post', backref='creator')
	response = db.relationship('Response', backref='creator')
	
	groups = db.relationship(
        'Group', secondary=group_associations)
        
	def as_dict(self):
		ndict = {}
		ndict['id'] = self.id
		ndict['first_name'] = self.first_name
		ndict['last_name'] = self.last_name
		ndict['email'] = self.email
		ndict['about'] = self.about
		ndict['password_hashed'] = self.password_hashed
		ndict['username'] = self.username
		
		return ndict
        
	def add_to_group(self, group):
		if not self.in_group(group):
			self.groups.append(group)
			db.session.commit()
		
		
	def remove_from_group(self, group):
		if self.in_group(group):
			self.group.remove(group)
			db.session.commit()
		
	def in_group(self, group):
		#return self.groups.filter(group_associations.c.group_id == group.id).count() > 0
		return group in self.groups
		# I really don't see why we can't just do return group in self.groups
		
	def is_admin(self):
		return Group.admin_group() in self.groups
	
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
	content = db.Column(db.Text(current_config.app_message_max_length), index=True)
	
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) 
	
	topics = db.Column(db.Text(current_config.app_message_max_length), index=True, default="")	
	
	response = db.relationship("Response", backref="parent_post", lazy="dynamic")
	
	def get_topics_list(self):
		return json.loads(self.topics)
	
	

	def __repr__(self):
		return "<object Post {} {}>".format(self.id, self.title)
		
		
		
		
class Response(db.Model):
	__tablename__ = "responses"
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	
	
	response_subresponses = db.relationship(
        'Response', secondary=subresponses,
        primaryjoin=(subresponses.c.response_id == id),
        secondaryjoin=(subresponses.c.subresponse_id == id),
        backref=db.backref('subresponses', lazy='dynamic'), lazy='dynamic')
	
	post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
	
	content = db.Column(db.Text(current_config.app_message_max_length))
	
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	
	
	def add_subresponse(self, subresponse):
		if not self.is_subresponse(subresponse):
			self.response_subresponses.append(subresponse)
		
	def remove_subresponse(self, subresponse):
		if self.is_subresponse(subresponse):
			self.response_subrepsonses.remove(subresponse)
	
	def is_subresponse(self, subresponse): #we'll not be removing the subresponse param because the program is more flexible then
		return self.subresponses.filter(
			subresponses.c.subresponse_id == subresponse.id).count() > 0
	
	
	def __repr__(self):
		return "<object Response id:{}>".format(self.id)

class Group(db.Model):
	__tablename__ = 'groups'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(256), index=True)
	
	def formatted_name(self):
		return self.name.replace(" ", "_").lower()
	
	@staticmethod
	def create_group(group_name):
		new_group = Group(name=group_name)
		db.session.add(new_group)
		db.session.commit()
	
	
	@staticmethod	
	def admin_group():
		return Group.query.filter_by(id=current_config.app_admin_group_id).first() # TODO Force group admin to be created with GID 1
		
	def __repr__(self):
		return "<Group id: {} name: {}".format(id, self.name)
		
		
class DBConfig(db.Model):
	__tablename__ = 'config'
	
	config_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	
	key = db.Column(db.String(128), index=True)
	value = db.Column(db.Text(9999))	
	@staticmethod
	def get_value(key):
		return DBConfig.query.filter_by(key=key).first()
		


	
		

		
		
	
		


