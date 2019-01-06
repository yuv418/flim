from app.models import Topic, DBConfig
from app import config

from app import db

# Prevent flask from breaking itself if the db is not installed yet.
from sqlalchemy.exc import ProgrammingError

current_config = config.Config()

def get_full_post_topics_list():
	config_topics_list = current_config.get_post_topics_list()
	
	#print('Topic list {}'.format(Topic.query.all()))
	try:
		db_topics_list = [(topic.name, topic.name) for topic in Topic.query.all()]
	except ProgrammingError:
		# Set a blank list if the db is not initialized
		db_topics_list = []
	
	#for topic in db_topics_list:
		#print(topic)
			
	return config_topics_list + db_topics_list
	
def add_config_keypair(key, value):
	prev_config_chk = DBConfig.query.filter_by(key=key).first()
	
	if prev_config_chk == None: # There is no previous config row with this key in the database, add it
		new_config = DBConfig(key=key, value=value)
		db.session.add(new_config)
	
	else: # This config row exists, update it.
		prev_config_chk.value = value
	
	print(f"Adding new config set: {key}: {value}")
	
	db.session.commit() # Commit our changes to the database

def get_config_value(key):
	config = DBConfig.query.filter_by(key=key).first()
	
	if config == None: # If this doesn't exist yet in the database
		return -1
	
	return config.value
