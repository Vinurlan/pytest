from flask_sqlalchemy import SQLAlchemy
from application import app

db = SQLAlchemy(app)

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    sname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1))
    email = db.Column(db.String(120))
    traningplan = db.Column(db.String(240))

    def __init__(self, fname, sname, age, gender, email, traningplan):
        self.fname = fname
        self.sname = sname
        self.age = age
        self.gender = gender
        self.email = email
        self.traningplan = traningplan

class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    sname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    email = db.Column(db.String(120))

    def __init__(self, fname, sname, age, gender, email):
        self.fname = fname
        self.sname = sname
        self.age = age
        self.gender = gender
        self.email = email