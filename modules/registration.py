from lib import StaffReg,StudentReg,app,db

def student_registration(rollno, name, mail, password):
    if db.session.query(StudentReg).filter(StudentReg.rollno == rollno).count() == 0:
        data = StudentReg(rollno, name, mail, password)
        db.session.add(data)
        db.session.commit()  
        return True
    else:
        return False

def staff_registration(staff_id, name, mail, dept, tutor, password):
    if db.session.query(StaffReg).filter(StaffReg.staff_id == staff_id).count() == 0:
        data = StaffReg(staff_id, name, mail, dept, tutor, password)
        db.session.add(data)
        db.session.commit()  
        return True
    else:
        return False