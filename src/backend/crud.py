"""
crud.py
Database operations using SQLAlchemy.
"""
from sqlalchemy.orm import Session
from backend.models import Customer, Prediction


def create_customer(db: Session, customer: Customer):
    """
    Insert a new customer into the database.
    """
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def get_customer(db: Session, customer_id: str):
    """
    Fetch a customer by customerID.
    """
    return (
        db.query(Customer)
        .filter(Customer.customerID == customer_id)
        .first()
    )


def get_all_customers(db: Session):
    """
    Fetch all customers.
    """
    return db.query(Customer).all()


def update_customer(db: Session, customer_id: str, updated_data: dict):
    """
    Update customer details.
    """
    customer = (
        db.query(Customer)
        .filter(Customer.customerID == customer_id)
        .first()
    )
    if customer:
        for key, value in updated_data.items():
            setattr(customer, key, value)

        db.commit()
        db.refresh(customer)

    return customer


def delete_customer(db: Session, customer_id: str):
    """
    Delete a customer.
    """
    customer = (
        db.query(Customer)
        .filter(Customer.customerID == customer_id)
        .first()
    )

    if customer:
        db.delete(customer)
        db.commit()

    return customer

def save_prediction(db: Session, prediction: Prediction):
    """
    Save a prediction to the database.
    """
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction


def get_prediction(db: Session, prediction_id: int):
    """
    Fetch a prediction by its ID.
    """
    return (
        db.query(Prediction)
        .filter(Prediction.id == prediction_id)
        .first()
    )


def get_prediction_history(db: Session, customer_id: str):
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