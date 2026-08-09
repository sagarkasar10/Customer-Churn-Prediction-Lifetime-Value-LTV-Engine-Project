"""
main.py
Entry point of the Customer Churn Prediction & LTV Engine backend.
"""
import logging
from fastapi import FastAPI, Depends, HTTPException, Query

from sqlalchemy.orm import Session

from src.backend import crud
from src.backend.models import Customer
from src.schemas.customer import Customer as CustomerSchema

from src.backend.config import APP_NAME, APP_VERSION
from src.backend.database import get_db, Base, engine
from src.backend.model_loader import load_model
from src.routers import single_predict


logging.basicConfig(level=logging.INFO)

try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    logging.error(f"Could not initialize database schema: {e}")

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


@app.post("/customers")
def create_customer(
    customer: CustomerSchema,
    db: Session = Depends(get_db)
):
    """
    Create a new customer.
    """
    if crud.customer_exists(
        db,
        customer.customerID
    ):
        raise HTTPException(
            status_code=400,
            detail="Customer already exists"
        )
    db_customer = Customer(
        **customer.model_dump()
    )
    return crud.create_customer(
        db,
        db_customer
    )


@app.get("/customers/paginated")
def get_customers_paginated(skip: int = Query(0), limit: int = Query(20), db: Session = Depends(get_db)):
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


@app.put("/customers/{customer_id}")
def update_customer(
    customer_id: str,
    customer: CustomerSchema,
    db: Session = Depends(get_db)
):
    """
    Update customer details.
    """

    updated_customer = crud.update_customer(
        db,
        customer_id,
        customer.model_dump()
    )

    if not updated_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return updated_customer


@app.delete("/customers/{customer_id}")
def delete_customer(
    customer_id: str,
    db: Session = Depends(get_db)
):
    """
    Delete customer.
    """

    customer = crud.delete_customer(
        db,
        customer_id
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {
        "message": "Customer deleted successfully"
    }


@app.get("/predictions")
def get_predictions(db: Session = Depends(get_db)):
    """
    Retrieve all predictions.
    """
    return crud.get_all_predictions(db)


@app.get("/predictions/{customer_id}")
def get_customer_predictions(customer_id: str, db: Session = Depends(get_db)):
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

app.include_router(single_predict.router)
