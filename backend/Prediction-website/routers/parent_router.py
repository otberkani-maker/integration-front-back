from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import Parent, Student
from schemas.schemas import ParentCreate, ParentLogin, ParentResponse, Token
from utils.auth import verify_password, get_password_hash, create_access_token
from datetime import timedelta

router = APIRouter(prefix="/parents", tags=["parents"])

@router.post("/register", response_model=ParentResponse)
def register_parent(parent: ParentCreate, db: Session = Depends(get_db)):
    if db.query(Parent).filter(Parent.email == parent.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if not db.query(Student).filter(Student.student_id == parent.student_id).first():
        raise HTTPException(status_code=400, detail="Student not found")
    hashed_password = get_password_hash(parent.password)
    db_parent = Parent(
        email=parent.email,
        phone_number=parent.phone_number,
        student_id=parent.student_id,
        password_hash=hashed_password
    )
    db.add(db_parent)
    db.commit()
    db.refresh(db_parent)
    return {"parent_id": db_parent.parent_id, "email": db_parent.email, "phone_number": db_parent.phone_number, "student_id": db_parent.student_id}

@router.post("/login", response_model=Token)
def login_parent(email: str = Query(...), password: str = Query(...), db: Session = Depends(get_db)):
    db_parent = db.query(Parent).filter(Parent.email == email).first()
    if not db_parent or not verify_password(password, db_parent.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": str(db_parent.parent_id), "role": "parent"}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "role": "parent"}
