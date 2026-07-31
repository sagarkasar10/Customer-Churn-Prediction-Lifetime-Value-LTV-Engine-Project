"""
crud.py
CRUD (Create, Read, Update, Delete) operations
for Customer and Prediction tables.
"""

from sqlalchemy.orm import Session
from backend.models import Customer, Prediction


#Customer table
def create_customer(db: Session, customer: Customer):
    """
    Add a new customer into the database.
    """
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def get_all_customers(db: Session):
    """
    Fetch all customers.
    """
    return db.query(Customer).all()


def get_customer_by_id(db: Session, customer_id: str):
    """
    Fetch a customer by customerID.
    """
    return (
        db.query(Customer)
        .filter(Customer.customerID == customer_id)
        .first()
    )


def count_customers(db: Session):
    """
    Return total number of customers.
    """
    return db.query(Customer).count()


def customer_exists(db: Session, customer_id: str):
    """
    Check whether a customer exists.
    """
    return (
        db.query(Customer)
        .filter(Customer.customerID == customer_id)
        .first()
    )


def get_customers_by_tenure(db: Session):
    """
    Return customers sorted by tenure in descending order.
    """
    return (
        db.query(Customer)
        .order_by(Customer.tenure.desc())
        .all()
    )


#Prediction table
def create_prediction(db: Session, prediction: Prediction):
    """
    Save a prediction to the database.
    """
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction


def get_all_prediction(db: Session):
    """
    Retrieve all prediction records.
    """
    return db.query(Prediction).all()


def get_prediction_by_customer(db: Session, customer_id: str):
    """
    Fetch all predictions for a customer.
    """
    return (
        db.query(Prediction)
        .filter(Prediction.customerID == customer_id)
        .all()
    )


def delete_prediction(db: Session, prediction_id: int):
    """
    Delete a prediction.
    """
    prediction = (
        db.query(Prediction)
        .filter(Prediction.id == prediction_id)
        .first()
    )

    if prediction:
        db.delete(prediction)
        db.commit()

    return prediction


def get_customers_paginated(
    db: Session,
    skip: int = 0,
    limit: int = 20
):
    """
    Return customers using pagination.
    """

    return (
        db.query(Customer)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_customers_by_contract(
    db: Session,
    contract: str
):
    """
    Return customers with given contract type.
    """

    return (
        db.query(Customer)
        .filter(Customer.Contract == contract)
        .all()
    )


def get_customers_by_internet_service(
    db: Session,
    service: str
):
    """
    Return customers using given internet service.
    """

    return (
        db.query(Customer)
        .filter(Customer.InternetService == service)
        .all()
    )