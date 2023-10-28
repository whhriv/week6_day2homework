
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

app.config.from_object(Config)
print(app.config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

#REGISTER THE API BLUEPRINT WITHOUT APP
from app.blueprints.api import api
app.register_blueprint(api)

from . import routes, models