from datetime import datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Person(db.Model):
    __tablename__= "Person"
    Id = db.Column(db.Integer, primary_key=True)
    Förnamn = db.Column(db.String(50), unique=False, nullable=False)
    Efternamn = db.Column(db.String(50), unique=False, nullable=False)
    Address = db.Column(db.String(50), unique=False, nullable=False)
    Stad = db.Column(db.String(50), unique=False, nullable=False)

    Accounts = db.relationship('Account', backref='Person',lazy=True)





class Account(db.Model):
    __tablename__= "Accounts"
    Id = db.Column(db.Integer, primary_key=True)
    Kontotyp = db.Column(db.String(10), unique=False, nullable=False)
    Skapad = db.Column(db.DateTime, unique=False, nullable=False, default= datetime.utcnow)
    Saldo = db.Column(db.Integer, unique=False, nullable=False)
    PersonId = db.Column(db.Integer, db.ForeignKey('Person.Id'), nullable=False)
