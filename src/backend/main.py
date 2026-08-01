"""
main.py
Entry point of the Customer Churn Prediction & LTV Engine backend.
"""
import logging
from fastapi import FastAPI, Depends, HTTPException, Query

from sqlalchemy.orm import Session

from backend import crud
from backend.config import APP_NAME, APP_VERSION
from backend.database import get_db, Base, engine
from backend.models import Customer, Prediction
from backend.model_loader import load_model


logging.basicConfig(level=logging.INFO)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title=APP_NAME,
    description="Backend API for Customer Churn Prediction & Lifetime Value Estimation",
    version=APP_VERSION,
)


@app.on_event("startup")
def startup():
    """
    Load ML model when backend starts.
    """
    load_model()



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


@app.get("/customers/count")
def count_customers(db: Session = Depends(get_db)):
    """
    Return total number of customers.
    """
    return {
        "total_customers": crud.count_customers(db)
    }


@app.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    """
    Retrieve all customers.
    """
    return crud.get_all_customers(db)


@app.get("/customers/{customer_id}")
def get_customer(customer_id: str,
                 db: Session = Depends(get_db)):
    """
    Retrieve customer by customerID.
    """

    customer = crud.get_customer_by_id(
        db,
        customer_id
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@app.get("/predictions")
def get_predictions(db: Session = Depends(get_db)):
    """
    Retrieve all predictions.
    """
    return crud.get_all_predictions(db)


@app.get("/predictions/{customer_id}")
def get_customer_predictions(
    customer_id: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve prediction history for one customer.
    """
    predictions = crud.get_predictions_by_customer(
        db,
        customer_id
    )
    if not predictions:
        raise HTTPException(
            status_code=404,
            detail="No predictions found"
        )

    return predictions


@app.get("/customers/paginated")
def get_customers_paginated(
    skip: int = Query(0),
    limit: int = Query(20),
    db: Session = Depends(get_db)
):
    return crud.get_customers_paginated(
        db,
        skip,
        limit
    )


@app.get("/customers/contract/{contract}")
def get_customers_by_contract(
    contract: str,
    db: Session = Depends(get_db)
):
    return crud.get_customers_by_contract(
        db,
        contract
    )


@app.get("/customers/internet/{service}")
def get_customers_by_internet(
    service: str,
    db: Session = Depends(get_db)
):
    return crud.get_customers_by_internet_service(
        db,
        service
    )