from flask import Flask
from app import config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import config

current_config = config.Config()

app = Flask(__name__, static_url_path=current_config.app_static_files_directory)
app.config.from_object(current_config)

login = LoginManager(app)
login.login_view='login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
