import os

class Config:
	
	
	app_name = "Flim"
	app_allow_anonymous_view_posts = True #TODO actually make this work
	
	app_db_name = "bug_reporter_db"
	app_db_username = "default_u"
	app_db_password = "letmeinmysql"
	app_db_host = "localhost"
	
	app_post_topics_list = [("Announcement", "Announcement"), ("Help Needed", "Help Needed"), ("Idea", "Idea"), ("Not Urgent", "Not Urgent"), ("Urgent", "Urgent"), ("Windows", "Windows"), ("macOS", "macOS"), ("Linux", "Linux"),
		("iOS", "iOS"), ("Android", "Android"), ("Windows Phone", "Windows Phone"), ("SIM Card Problem", "SIM Card Problem"), ("Phone", "Phone"), ("Desktop", "Desktop"), ("Laptop", "Laptop"),
		("Broken", "Broken"), ("Data Recovery", "Data Recovery")] 
		
	
	
	
	# DO NOT EDIT THE FOLLOWING!!!!!
	
	app_static_files_directory = "/static" # do not change, just makes things easier for us
	
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'afioj89498ffj98hiahffuihfihwilafhliuifhUIHFIUHFIUHfieuahhu8yh4ih4foh'
	SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}/{}".format(app_db_username, app_db_password, app_db_host, app_db_name)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
