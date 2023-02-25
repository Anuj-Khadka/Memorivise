from flask_login import UserMixin
from datetime import datetime
from . import db


class Revise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'{self.id} - {self.text}'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    revise = db.relationship('Revise')
    
class Memorivise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.string, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'{self.sno} - {self.document}'

<<<<<<< HEAD
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_email = db.Column(db.String, nullable=False)
    contact_name = db.Column(db.String, nullable=False)
    contact_message = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

=======

class Memorivise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.string, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'{self.sno} - {self.document}'
>>>>>>> a7bafb3800bb03578241e37458f62de16792bef9
