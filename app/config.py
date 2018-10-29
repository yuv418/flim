import os

class Config:
	
	#************************ THE FOLLOWING SETTINGS **CANNOT BE** TO BE EDITABLE OUT OF THE CONFIG FILE *********************************************************
	
	
	app_name = "Flim"
	app_allow_anonymous_view_posts = True #TODO actually make this work
	
	app_db_name = "flimdb" # no edits outside of config file.
	app_db_username = "default_u" # no edits outside of config file.
	app_db_password = "letmeinmysql" # no edits outside of config file.
	app_db_host = "localhost" # no edits outside of config file.
	app_db_provider = "mysql" # no edits outside of config file.
	
	app_message_max_length = 9990 # no edits outside of config file.
		
	
	#************************ END SECTION *********************************************************
	
	
	
	#************************ THE FOLLOWING SETTINGS HAVE TO BE EDITABLE OUT OF THE CONFIG FILE *********************************************************
	
	
	
	app_post_topics_list = ["Announcement", "Help Needed", "Idea", "Not Urgent", "Urgent", "Windows", "macOS", "Linux", "iOS", "Android", "Windows Phone", 
		"Ubuntu Touch", "KDE Plasma Mobile", "Question", "SIM Card Problem", "Cell Phone", "Desktop", "Laptop", "Broken", "Data Recovery"] # allow edits outside of config file.
	
	app_allow_registration = True # allow edits outside of config file.
	
	app_admin_group_id = 1 # allow edits outside of config file.
	
	#************************ END SECTION *********************************************************
	
	
	
	
	# DO NOT EDIT THE FOLLOWING!!!!!
	
	app_version = "TESTING"
	app_static_files_directory = "/static" # do not change, just makes things easier for us
	
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'afioj89498ffj98hiahffuihfihwilafhliuifhUIHFIUHFIUHfieuahhu8yh4ih4foh'
	SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}/{}".format(app_db_provider, app_db_username, app_db_password, app_db_host, app_db_name)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	
	def get_post_topics_list(self):
		config_topics_list = [(topic, topic) for topic in self.app_post_topics_list]
		return config_topics_list
