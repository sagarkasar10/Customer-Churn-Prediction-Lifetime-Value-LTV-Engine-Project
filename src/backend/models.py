"""
models.py

SQLAlchemy ORM models for the Customer Churn Prediction & LTV Engine.
"""

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from src.backend.database import Base


class Customer(Base):
    """
    Represents the customers table.
    """

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    customerID = Column(
        String(50), 
        unique=True, 
        nullable=False,
        index=True
    )

    gender = Column(String(10))

    SeniorCitizen = Column(Integer)

    Partner = Column(String(5))

    Dependents = Column(String(5))

    tenure = Column(Integer)

    PhoneService = Column(String(5))

    InternetService = Column(String(30))

    Contract = Column(String(30))

    PaymentMethod = Column(String(50))

    MonthlyCharges = Column(Float)

    TotalCharges = Column(Float)

    MultipleLines = Column(String(30))

    OnlineSecurity = Column(String(30))

    OnlineBackup = Column(String(30))

    DeviceProtection = Column(String(30))

    TechSupport = Column(String(30))

    StreamingTV = Column(String(30))

    StreamingMovies = Column(String(30))

    PaperlessBilling = Column(String(5))


    # Relationship with Prediction table
    predictions = relationship(
        "Prediction",
        back_populates="customer",
        cascade="all, delete-orphan"
    )


class Prediction(Base):
    """
    Represents model predictions for each customer.
    """

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    customerID = Column(
        String(50),
        ForeignKey("customers.customerID"),
        nullable=False,
        index=True
    )

    predicted_churn = Column(String(10))

    predicted_ltv = Column(Float)

    prediction_time = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # Relationship back to Customer
    customer = relationship(
        "Customer",
        back_populates="predictions"
    )