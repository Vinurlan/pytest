from flask import render_template, request
import json
from db import db, Clients, Trainer, traningplan
from app import app
from flask_cors import CORS

# CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})
CORS(app, resources={r"/api/*": {"origins": "*"}})

# @app.route('/')
# def home():
#     clients = Clients.query.all()
#     return render_template("index.html", list=traningplan, clients=clients)

# Trainers
@app.route("/api/trainers/all")
def trainerall():
    trainers = Trainer.query.all()
    result = []

    for item in trainers:
        result.append({
            'firstName': item.fname,
            'lastName': item.sname,
            'age': item.age,
            'gender': item.gender,
            'email': item.email,
        })

    return result

@app.route("/api/trainers/add", methods=['POST'])
def traineradd():
    data = request.get_json()
    
    fname = data['firstName']
    sname = data['lastName']
    age = data['age']
    gender = data['gender']
    email = data['email']

    entry = Trainer(fname, sname, age, gender, email)
    db.session.add(entry)
    db.session.commit()

    result = {
        'status': 200,
        'data': data
    }

    return result

# Clients
@app.route("/api/clients/all")
def clientall():
    clients = Clients.query.all()
    result = []

    for item in clients:
        result.append({
            'id': item.id,
            'firstName': item.fname,
            'lastName': item.sname,
            'age': item.age,
            'gender': item.gender,
            'email': item.email,
            'plan': item.traningplan,
        })

    return result

@app.route("/api/clients/add", methods=['POST'])
def clientadd():
    data = request.get_json()
    
    fname = data['firstName']
    sname = data['lastName']
    age = data['age']
    gender = data['gender']
    email = data['email']

    if 'traningplan' in data:
        traningplan = data['traningplan']
    else: 
        traningplan = ''

    entry = Clients(fname, sname, age, gender, email, traningplan)
    db.session.add(entry)
    db.session.commit()

    result = {
        'status': 200,
        'data': data
    }

    return result

@app.route("/api/clients/edit", methods=['PUT'])
def clientedit():
    data = request.get_json()
    cid = data['id']

    clients = Clients.query.find(id=cid)
    
    clients.fname = data['firstName']
    clients.sname = data['lastName']
    clients.age = data['age']
    clients.gender = data['gender']
    clients.email = data['email']

    if 'traningplan' in data:
        clients.traningplan = data['traningplan']
    else: 
        clients.traningplan = ''

    db.session.commit()

    result = {
        'status': 200,
        'data': data
    }

    return result