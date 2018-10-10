from app.models import Post
from app import db

import json

class NewPost:
	def __init__(self, user_id, title="", content="", topics=[]):
		self.user_id = user_id
		self.title = title
		self.content = content
		self.topics = topics
		
	def create_new_post(self):
		new_post = Post(user_id=self.user_id,
			title=self.title,
			content=self.content,
			topics=json.dumps(self.topics))
		
		db.session.add(new_post)
		db.session.commit()
		
		return new_post.id
		
