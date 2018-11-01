from app.models import Topic, DBConfig
from app import config

from app import db

current_config = config.Config()

def get_full_post_topics_list():
	config_topics_list = current_config.get_post_topics_list()
	
	print('Topic list {}'.format(Topic.query.all()))
	
	db_topics_list = [(topic.name, topic.name) for topic in Topic.query.all()]
	
	for topic in db_topics_list:
		print(topic)
			
	return config_topics_list + db_topics_list
	
def add_config_keypair(key, value):
	new_config = DBConfig(key=key, value=value)
	
	print(f"Adding new config set: {key}: {value}")
	
	db.session.add(new_config)
	db.session.commit()
