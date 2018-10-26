from app.models import Topic
from app import config

current_config = config.Config()

def get_full_post_topics_list():
	config_topics_list = current_config.get_post_topics_list()
	db_topics_list = [(topic.name, topic.name) for topic in Topic.query.all()]
			
	return config_topics_list + db_topics_list
