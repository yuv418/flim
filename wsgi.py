import sys
import os

sys.path.append(os.getcwd() + "/app")
from app import app, config, db

current_config = config.Config()
db.create_all()

if __name__ == "__main__":
	app.run(host = current_config.app_host)
