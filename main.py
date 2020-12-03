from flask_sqlalchemy import SQLAlchemy
from modules.login_val import student_login_validation,staff_login_validation
from modules.registration import student_registration,staff_registration
from modules.sendmail import send_credentials
from flask import render_template,request,jsonify, make_response
from lib import app

@app.route("/register_staff",methods=['POST'])
def staff_reg():
    staff_id = request.form['staff_id']
    name = request.form['name']
    mail = request.form['mail']
    dept = request.form['dept'] 
    tutor = request.form['tutor']
    password = request.form['password']
    if staff_registration(staff_id, name, mail, dept, tutor, password):
        return make_response(jsonify(
            {
                'status' : 'success',
                'desc':'staff got registered',
                'result' : {}
            }
        ), 200)
    
    else:
        #render_template('staff_register.html',message='staff already registered')
        return make_response(jsonify(
            {
                'status' : 'fail',
                'desc':'staff already registered',
                'result' : {}
            }
        ), 200)

@app.route("/register_student",methods=['POST'])
def student_reg():
    rollno = request.form['rollno']
    name = request.form['name']
    mail = request.form['mail']
    password = request.form['password']
    if student_registration(rollno, name, mail, password):
        return make_response(jsonify(
            {
                'status' : 'success',
                'desc':'student got registered',
                'result' : {}
            }
        ), 200)
    else:
        #render_template('student_register.html',message='student already registered')
        return make_response(jsonify(
            {
                'status' : 'fail',
                'desc':'student already registered',
                'result' : {}
            }
        ), 200)

@app.route("/staff_login",methods=['POST'])
def staff_login():
    staffdata = request.get_json()
    username = staffdata['staff_id']
    password = staffdata['password']
    if staff_login_validation(username,password):
        #render_template('staff_home.html',message='you got registered',staff_id = staffdata['staff_id'])
        return make_response(jsonify(
            {
                'status' : 'success',
                'desc':'log-in successfull',
                'result' : {}
            }
        ), 200)
    else:
        #render_template('staff_login.html',message='you got registered')
        return make_response(jsonify(
            {
                'status' : 'success',
                'desc':'log-in failed',
                'result' : {}
            }
        ), 200)
    
@app.route("/student_login",methods=['POST'])
def student_login():
    studentdata = request.get_json()
    username = studentdata['rollno']
    password = studentdata['password']
    if student_login_validation(username,password):
        #render_template('student_home.html',message='validation failed', rollno=studentdata['rollno'])
        return make_response(jsonify(
            {
                'status' : 'success',
                'desc':'log-in successfull',
                'result' : {}
            }
        ), 200)
    else:
        #render_template('staff_login.html',message='you got registered')
        return make_response(jsonify(
            {
                'status' : 'success',
                'desc':'incorrect password',
                'result' : {}
            }
        ), 200)

@app.route('/forget_credentials',methods=['Post'])
def forget_cred():
    mail = request.form['email']
    status = send_credentials(mail)
    if status:
        return {'desc':"check your mail"}
    else:
        return {'desc':"There is no account linked with this email ID , please enter a registered email ID"}


    
    
