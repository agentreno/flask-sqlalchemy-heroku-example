import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Person(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   firstname = db.Column(db.String(30))
   lastname = db.Column(db.String(40))
   dateofbirth = db.Column(db.String(10))
   zipcode = db.Column(db.String(10))

   def __init__(self, firstname, lastname, dateofbirth, zipcode):
      self.firstname = firstname
      self.lastname = lastname
      self.dateofbirth = dateofbirth
      self.zipcode = zipcode

db.create_all()
p = Person("Karl", "HT", "31/08/1987", "12345")
db.session.add(p)
db.session.commit()

@app.route("/")
def home():
   return str(Person.query.all())
