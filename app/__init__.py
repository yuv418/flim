from flask import Flask
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import config

current_config = config.Config()

app = Flask(__name__)
app.config.from_object(current_config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
