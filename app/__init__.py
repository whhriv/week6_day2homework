from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['secrets'] = 'thats-it-the-rebels-are-there'
app.config.from_object(Config)
print(app.config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
from . import routes