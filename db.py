from flask_sqlalchemy import SQLAlchemy
from app import app

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


traningplan = {
    'пн': ['жим от груди - 50кг - 1 подход - 12 повторений'],
    'вт': [],
    'ср': ['спина - 20кг - 2 подхода - 10 повторений'],
    'чт': [],
    'пт': ['ноги - сгибание - 35кг - 3 подхода - 15 повторений'],
    'сб': [],
    'вс': [],
}