from flask import Flask

from app import config

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow




current_config = config.Config()

app = Flask(__name__, static_url_path=current_config.app_static_files_directory)
app.config.from_object(current_config)

login = LoginManager(app)
login.login_view='login'

db = SQLAlchemy(app)
ma = Marshmallow(app)
nmigrate = Migrate(app, db)

api = Api(app)


from app import routes

