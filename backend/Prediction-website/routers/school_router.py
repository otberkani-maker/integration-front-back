from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import School
from schemas.schemas import SchoolCreate, SchoolLogin, SchoolResponse, Token
from utils.auth import verify_password, get_password_hash, create_access_token
from datetime import timedelta

router = APIRouter(prefix="/schools", tags=["schools"])

@router.post("/register", response_model=SchoolResponse)
def register_school(school: SchoolCreate, db: Session = Depends(get_db)):
    # Check if email exists
    db_school = db.query(School).filter(School.email == school.email).first()
    if db_school:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(school.password)
    db_school = School(
        name=school.name,
        address=school.address,
        email=school.email,
        password_hash=hashed_password
    )
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

@router.post("/login", response_model=Token)
def login_school(email: str = Query(...), password: str = Query(...), db: Session = Depends(get_db)):
    db_school = db.query(School).filter(School.email == email).first()
    if not db_school or not verify_password(password, db_school.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": str(db_school.school_id), "role": "school"}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "role": "school"}