from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import local_engine,heroku_engine,local

app=Flask(__name__)

if local:
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']=local_engine
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']=heroku_engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
 
class StaffReg(db.Model):
    __tablename__ = 'staffreg'
    staff_id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(200))
    mail = db.Column(db.String(200))
    dept = db.Column(db.String(200))
    tutor = db.Column(db.String(10))
    password = db.Column(db.String(200))

    def __init__(self, staff_id, name, mail, dept, tutor, password):
        self.staff_id = staff_id
        self.name = name
        self.mail = mail
        self.dept = dept
        self.tutor = tutor
        self.password = password


class StudentReg(db.Model):
    __tablename__ = 'studentreg'
    rollno = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(200))
    mail = db.Column(db.String(200))
    password = db.Column(db.String(200))

    def __init__(self, rollno, name, mail, password):
        self.rollno = rollno
        self.name = name
        self.mail = mail
        self.password = password