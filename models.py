from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import app, db
from datetime import datetime

db = SQLAlchemy()

class Revise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'{self.id} - {self.text}'


class User(db.Model, UserMixin):
    id = db.Column(db.Interger, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    revise = db.relationship('Revise')