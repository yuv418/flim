from app import db

class Users(db.Model):
	tablename='users'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(128), index=True, unique=True)
	last_name = db.Column(db.String(128), index=True, unique=True)
	email = db.Column(db.Text, index=True, unique=True)
	password_hashed = db.Column(db.String(256), index=True, unique=True)
	username = db.Column(db.String(32), index=True, unique=True)
	
	def __repr__(self):
		return "<object User {}>".format(self.username)
