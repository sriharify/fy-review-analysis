from lib import StaffReg,StudentReg,app,db
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_credentials(mail):
    studentdata = db.session.query(StudentReg).filter(StudentReg.mail == mail).all() 
    staffdata = db.session.query(StaffReg).filter(StaffReg.mail == mail).all()
    username = None
    password = None
    if len(studentdata)==1:
        username = studentdata[0].rollno
        password = studentdata[0].password
    if len(staffdata)==1:
        username = staffdata[0].staff_id
        password = staffdata[0].password
    if username and password:
        email=mail
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.ehlo()
        s.starttls() 
        s.ehlo()
        s.login("frontyard.hotel.bi@gmail.com", "hotelbi@123")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Here is your credentials '
        msg['From'] = "frontyard.hotel.bi@gmail.com"
        msg['To'] = email
        body = "Your user id is "+ username+" and your password is "+password
        body = MIMEText(body,'html')
        msg.attach(body) 
        s.sendmail("frontyard.hotel.bi@gmail.com", email, msg.as_string()) 
        s.quit()
        msg="check the mail"
        return True
    else:
        return False