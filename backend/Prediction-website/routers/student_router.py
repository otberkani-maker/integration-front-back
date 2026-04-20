from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import Student, School
from schemas.schemas import StudentCreate, StudentLogin, StudentResponse, Token
from utils.auth import verify_password, get_password_hash, create_access_token
from datetime import timedelta

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/register", response_model=StudentResponse)
def register_student(student: StudentCreate, db: Session = Depends(get_db)):
    if db.query(Student).filter(Student.email == student.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    db_school = db.query(School).filter(School.name == student.schoolName).first()
    if not db_school:
        raise HTTPException(status_code=400, detail="School not found. Make sure the school name matches exactly.")
    hashed_password = get_password_hash(student.password)
    db_student = Student(
        first_name=student.firstName,
        last_name=student.familyName,
        email=student.email,
        password_hash=hashed_password,
        grade=student.level,
        stream=student.studentPersonalId,
        school_id=db_school.school_id
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"student_id": db_student.student_id, "email": db_student.email, "first_name": db_student.first_name, "last_name": db_student.last_name, "grade": db_student.grade, "stream": db_student.stream, "attendance_rate": db_student.attendance_rate, "homework_rate": db_student.homework_rate}

@router.post("/login", response_model=Token)
def login_student(email: str = Query(...), password: str = Query(...), db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.email == email).first()
    if not db_student or not verify_password(password, db_student.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": str(db_student.student_id), "role": "student"}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "role": "student"}
