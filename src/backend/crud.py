"""
crud.py

Database operations using SQLAlchemy.
"""

from sqlalchemy.orm import Session
from backend.models import Customer


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