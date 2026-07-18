""" Entry point for the Customer Churn Prediction & LTV Engine backend.
This file initializes the FastAPI application and provides basic endpoints
to verify that the backend is running. """

from fastapi import FastAPI

# Create FastAPI application
app = FastAPI(
    title="Customer Churn Prediction & LTV Engine",
    description="Backend API for Customer Churn Prediction and Lifetime Value Estimation",
    version="1.0.0"
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
    """
    Health check endpoint.

    Used to verify that the backend service is active.
    """
    return {
        "status": "Healthy",
        "message": "Backend service is running successfully."
    }