from flask import Flask
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import config

config = config.Config()

app = Flask(__name__)
app.config.from_object(config)

#app['SQLALCHEMY_DATABASE_URI'] = "mysql://{}:{}@{}/{}".format(config.app_db_username, config.app_db_password, config.app_db_host, config.app_db_name)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
