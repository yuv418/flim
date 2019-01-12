import sys
import os

# We first add the path for the main application so that we do not have import errors.

sys.path.append(os.getcwd() + "/app")
from app import app, config, db

# We then retrieve the config so that we can start the web app on the right port and host.

current_config = config.Config()

# Then, we "create" the database. This will happen after an upgrade to flim. Normally, nothing will happen with db.create_all() unless there are database changes that need to be applied.

db.create_all()

if __name__ == "__main__":
	app.run(host = current_config.app_host, port = current_config.app_port)
