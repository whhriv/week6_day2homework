from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from . import api
from flask import request
from app import db
from app.models import User
#from .auth import basic_auth, token_auth

basic_auth = HTTPBasicAuth()

@api.route('/users', methods=["GET"] ) 
def get_users():
    users = db.session.execute(db.select(User)).scalars().all
    return [user.to_dict() for user in users]

@api.route('/users/<user_id>')
def get_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return ['errorpost not found']
    return user.to_dict()
