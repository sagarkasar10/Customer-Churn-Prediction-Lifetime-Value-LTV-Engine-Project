"""
crud.py
CRUD (Create, Read, Update, Delete) operations
for Customer and Prediction tables.
"""

from sqlalchemy.orm import Session
from src.backend.models import Customer, Prediction
from sqlalchemy.exc import SQLAlchemyError


def create_customer(db: Session, customer: Customer):
    """
    Add a new customer to the database.
    """
    try:
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer

    except SQLAlchemyError as e:
        db.rollback()
        raise e


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


def customer_exists(db: Session, customer_id: str) -> bool:
    """
    Check whether a customer exists.
    """

    customer = (
        db.query(Customer)
        .filter(Customer.customerID == customer_id)
        .first()
    )

    return customer is not None


def get_customers_by_tenure(db: Session):
    """
    Return customers sorted by tenure in descending order.
    """
    return (
        db.query(Customer)
        .order_by(Customer.tenure.desc())
        .all()
    )


def update_customer(
    db: Session,
    customer_id: str,
    updated_data: dict
):
    """
    Update customer information.
    """

    customer = (
        db.query(Customer)
        .filter(Customer.customerID == customer_id)
        .first()
    )

    if not customer:
        return None

    try:
        for key, value in updated_data.items():
            setattr(customer, key, value)

        db.commit()
        db.refresh(customer)

        return customer

    except SQLAlchemyError as e:
        db.rollback()
        raise e


def delete_customer(db: Session, customer_id: str):
    """
    Delete a customer by customerID.
    """

    customer = (
        db.query(Customer)
        .filter(Customer.customerID == customer_id)
        .first()
    )

    if customer:
        try:
            db.delete(customer)
            db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise e

    return customer


def create_prediction(db: Session, prediction: Prediction):
    """
    Save prediction into database.
    """
    try:
        db.add(prediction)
        db.commit()
        db.refresh(prediction)
        return prediction

    except SQLAlchemyError as e:
        db.rollback()
        raise e


def count_predictions(db: Session):
    """
    Return total predictions count.
    """
    return db.query(Prediction).count()


def get_all_predictions(db: Session):
    """
    Retrieve all prediction records.
    """
    return db.query(Prediction).all()


def get_predictions_by_customer(db: Session, customer_id: str):
    """
    Fetch all predictions for a customer.
    """
    return (
        db.query(Prediction)
        .filter(Prediction.customerID == customer_id)
        .all()
    )


def delete_prediction(db: Session, customer_id: str):
    """
    Delete a prediction record by customer ID.
    """
    prediction = (
        db.query(Prediction)
        .filter(Prediction.customerID == customer_id)
        .first()
    )
    if prediction:

        try:
            db.delete(prediction)
            db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise e

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
