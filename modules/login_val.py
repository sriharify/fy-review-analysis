from lib import StaffReg,StudentReg,app,db

def student_login_validation(username,password):
    data = db.session.query(StudentReg).filter(StudentReg.rollno == username).all() 
    if len(data)==1:
        data1 = data[0]
        if username == data1.rollno and password == data1.password: 
            return True
        else:
            return False
    else:
        return False

def staff_login_validation(username,password):
    data = db.session.query(StaffReg).filter(StaffReg.staff_id == username).all()
    if len(data)==1:
        data1=data[0]
        if username == data1.staff_id and password == data1.password: 
            return True
        else:
            return False
    else:
        return False