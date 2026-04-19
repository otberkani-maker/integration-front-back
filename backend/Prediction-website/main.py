from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import engine, Base
from routers import student_router, parent_router, school_router, admin_router
import os
from dotenv import load_dotenv

load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Prediction Website API",
    description="API for student prediction and academic guidance",
    version="1.0.0",
    docs_url=None,
    redoc_url=None
)

# Enable CORS for frontend integration
allowed_origins = [
    "http://localhost:5173",  # Vite dev server
    "http://localhost:3000",  # Alternative dev port
    "http://127.0.0.1:5173",
    "https://localhost:5173",
    os.getenv("FRONTEND_URL", "http://localhost:5173"),  # From environment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(student_router)
app.include_router(parent_router)
app.include_router(school_router)
app.include_router(admin_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"} 
