import pytest
from pydantic import ValidationError

from src.schemas.customer import Customer


def valid_customer():
    return {
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 12,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "No",
        "DeviceProtection": "Yes",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 75.5,
        "TotalCharges": 906.0
    }


def test_valid_schema():

    customer = Customer(**valid_customer())

    assert customer.tenure == 12


def test_invalid_tenure():

    data = valid_customer()
    data["tenure"] = -1

    with pytest.raises(ValidationError):
        Customer(**data)


def test_invalid_monthly_charge():

    data = valid_customer()
    data["MonthlyCharges"] = "abc"

    with pytest.raises(ValidationError):
        Customer(**data)


def test_missing_field():

    data = valid_customer()
    del data["Contract"]

    with pytest.raises(ValidationError):
        Customer(**data)