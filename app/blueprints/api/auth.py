from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app import db
from app.models import User
from datetime import datetime


basic_auth = HTTPBasicAuth()