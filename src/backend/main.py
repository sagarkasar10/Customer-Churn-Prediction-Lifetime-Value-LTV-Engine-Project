"""
main.py
Entry point of the Customer Churn Prediction & LTV Engine backend.
"""
from fastapi import FastAPI
from backend.config import APP_NAME, APP_VERSION
from backend.database import Base, engine
from backend.models import Customer

Base.metadata.create_all(bind=engine)


# Initialize FastAPI application
app = FastAPI(
    title=APP_NAME,
    description="Backend API for Customer Churn Prediction & Lifetime Value Estimation",
    version=APP_VERSION,
)


@app.get("/")
def home():
    """
    Root endpoint.
    """
    return {
        "project": APP_NAME,
        "status": "Backend Running",
        "version": APP_VERSION
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {
        "status": "Healthy",
        "backend": "Running"
    }