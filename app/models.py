from app import db
import base64
#from datetime import datetime
#from flask_login import UserMixin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False, unique=True)
    #date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'address': self.address
            #'Time' : self.date_created

        }


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False, unique=True)
    #date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #image_url = db.Column(db.String, default=random_photo)
    
    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'address': self.address
            # 'Time' : self.date_created

        }