from app import db
from app.models import Response

class NewSubResponse:
	def __init__(self, content, parent_response, creator):
		self.content = content
		self.parent_response = parent_response
		self.creator = creator
		
	def create_subpresponse(self):
		new_subresponse = Response(user_id=self.creator.id, post_id=self.parent_response.parent_post.id, content=self.content)
		self.parent_response.add_subresponse(new_subresponse)
		db.session.commit()
