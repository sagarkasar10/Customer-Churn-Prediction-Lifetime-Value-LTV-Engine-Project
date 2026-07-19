""" Entry point for the Customer Churn Prediction & LTV Engine backend.
This file initializes the FastAPI application and provides basic endpoints
to verify that the backend is running. """

from fastapi import FastAPI
from backend.config import APP_NAME, APP_VERSION

# Create FastAPI application
app = FastAPI(
    title=APP_NAME,
    description="Backend API for Customer Churn and Lifetime Value Prediction",
    version=APP_VERSION
)

# Home endpoint
@app.get("/")
def home():
    #Root endpoint.
    #Returns a welcome message and backend status.

    return {
        "project": "Customer Churn Prediction & LTV Engine",
        "status": "Backend Running",
        "version": "1.0.0"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    #Health check endpoint.
    #Used to verify that the backend service is active.
  

    return {
        "status": "Healthy",
        "message": "Backend service is running successfully."
    }
