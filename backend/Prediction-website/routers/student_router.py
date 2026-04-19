from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import Student
from schemas.schemas import StudentCreate, StudentLogin, StudentResponse, Token
from utils.auth import verify_password, get_password_hash, create_access_token
from datetime import timedelta

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/register", response_model=StudentResponse)
def register_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Check if email exists
    db_student = db.query(Student).filter(Student.email == student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create student
    hashed_password = get_password_hash(student.password)
    db_student = Student(
        email=student.email,
        password_hash=hashed_password,
        grade=student.level,  # Assuming level is grade
        school_id=1  # Placeholder
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

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