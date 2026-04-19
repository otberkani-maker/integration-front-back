# Student schemas
from pydantic import BaseModel, EmailStr
from typing import Optional
class StudentCreate(BaseModel):
    firstName: str
    familyName: str
    email: EmailStr
    studentId: str
    level: str
    stream: str
    password: str

class StudentLogin(BaseModel):
    email: EmailStr
    password: str

class StudentResponse(BaseModel):
    student_id: int
    email: str
    grade: Optional[str]
    attendance_rate: Optional[float]
    homework_rate: Optional[float]

    class Config:
        from_attributes = True

# Parent schemas
class ParentCreate(BaseModel):
    email: EmailStr
    phone_number: Optional[str]
    student_id: int
    password: str

class ParentLogin(BaseModel):
    email: EmailStr
    password: str

class ParentResponse(BaseModel):
    parent_id: int
    email: str
    phone_number: Optional[str]
    student_id: int

    class Config:
        from_attributes = True

# School schemas
class SchoolCreate(BaseModel):
    name: str
    address: str
    email: EmailStr
    password: str

class SchoolLogin(BaseModel):
    email: EmailStr
    password: str

class SchoolResponse(BaseModel):
    school_id: int
    name: str
    address: str
    email: str

    class Config:
        from_attributes = True

# Admin schemas (assuming admin is a user with role admin)
class AdminCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class AdminLogin(BaseModel):
    email: EmailStr
    password: str

class AdminResponse(BaseModel):
    user_id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str
    role: str