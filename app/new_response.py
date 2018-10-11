from app import db
from app.models import Response

class NewResponse:
	def __init__(self, parent_post, content):
		self.content = content
		self.parent_post = parent_post
		self.response = Response(content=self.content, post_id=self.parent_post.id)
		
	def add_response(self):
		db.session.add(self.response)
		db.session.commit()
