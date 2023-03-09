from flask import Flask

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/flasksql'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tester:tester@37.9.5.157:5432/tester'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'hi'
