from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from database.database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    role = Column(String(20), default='user')

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey('schools.school_id'), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    grade = Column(String(10), nullable=True)
    password_hash   = Column(String(128), nullable=False)
    attendance_rate = Column(Float, nullable=True, default=0.0)
    homework_rate   = Column(Float, nullable=True, default=0.0)

    
class Parent(Base):
    __tablename__ = 'parents'

    parent_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone_number = Column(String(20), nullable=True)
     password_hash   = Column(String(128), nullable=False)

class  School(Base):
    __tablename__ = 'schools'

    school_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    address = Column(String(200), nullable=False)
    password_hash   = Column(String(128), nullable=False)

class Prediction(Base):
    __tablename__ = 'predictions'

    prediction_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
    result = Column(String(50), nullable=False)
    advice = Column(Text, nullable=True)
    progress = Column(Text, nullable=True)
    stats = Column(Text, nullable=True)       

class Report(Base):
    __tablename__ = 'reports'
    report_id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey('schools.school_id'), nullable=False)
    prediction_id = Column(Integer, ForeignKey('predictions.prediction_id'), nullable=False)
    report_date = Column(DateTime, default=datetime.utcnow)
