import os

class Config:
	
	
	app_name = "Flim"
	app_allow_anonymous_view_posts = True #TODO actually make this work
	
	app_db_name = "bug_reporter_db"
	app_db_username = "default_u"
	app_db_password = "letmeinmysql"
	app_db_host = "localhost"
	app_db_provider = "mysql"
	
	app_message_max_length = 9990
		
	app_post_topics_list = ["Announcement", "Help Needed", "Idea", "Not Urgent", "Urgent", "Windows", "macOS", "Linux", "iOS", "Android", "Windows Phone", 
		"Ubuntu Touch", "KDE Plasma Mobile", "Question", "SIM Card Problem", "Cell Phone", "Desktop", "Laptop", "Broken", "Data Recovery"]
	
	app_allow_registration = True
	
	
	
	# DO NOT EDIT THE FOLLOWING!!!!!
	
	app_static_files_directory = "/static" # do not change, just makes things easier for us
	
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'afioj89498ffj98hiahffuihfihwilafhliuifhUIHFIUHFIUHfieuahhu8yh4ih4foh'
	SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}/{}".format(app_db_provider, app_db_username, app_db_password, app_db_host, app_db_name)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	
	def get_post_topics_list(self):
		return [(choice, choice) for choice in self.app_post_topics_list]
