from pydantic import BaseModel, Field, field_validator

class Customer(BaseModel):
    customerID: str = Field(..., description="Unique customer identifier", examples=["7590-VHVEG"])
    gender: str = Field(..., description="Customer gender (Female, Male)", examples=["Female"])
    SeniorCitizen: int = Field(..., ge=0, le=1, description="1 if senior citizen, 0 otherwise", examples=[0])
    Partner: str = Field(..., description="Whether customer has a partner (Yes, No)", examples=["Yes"])
    Dependents: str = Field(..., description="Whether customer has dependents (Yes, No)", examples=["No"])
    tenure: int = Field(..., ge=0, description="Months customer has stayed with company", examples=[1])
    PhoneService: str = Field(..., description="Whether customer has phone service (Yes, No)", examples=["No"])
    MultipleLines: str = Field(..., description="Multiple lines option status", examples=["No phone service"])
    InternetService: str = Field(..., description="Internet service provider (DSL, Fiber optic, No)", examples=["DSL"])
    OnlineSecurity: str = Field(..., description="Online security add-on status", examples=["No"])
    OnlineBackup: str = Field(..., description="Online backup add-on status", examples=["Yes"])
    DeviceProtection: str = Field(..., description="Device protection add-on status", examples=["No"])
    TechSupport: str = Field(..., description="Tech support add-on status", examples=["No"])
    StreamingTV: str = Field(..., description="Streaming TV add-on status", examples=["No"])
    StreamingMovies: str = Field(..., description="Streaming movies add-on status", examples=["No"])
    Contract: str = Field(..., description="Contract term (Month-to-month, One year, Two year)", examples=["Month-to-month"])
    PaperlessBilling: str = Field(..., description="Paperless billing status (Yes, No)", examples=["Yes"])
    PaymentMethod: str = Field(..., description="Payment method used", examples=["Electronic check"])
    MonthlyCharges: float = Field(..., gt=0, description="Monthly charge amount", examples=[29.85])
    TotalCharges: float = Field(..., ge=0, description="Total amount charged", examples=[29.85])

    @field_validator("Contract")
    @classmethod
    def validate_contract(cls, value: str) -> str:
        allowed = {"Month-to-month", "One year", "Two year"}
        if value not in allowed:
            raise ValueError(f"Invalid Contract value '{value}'. Must be one of {allowed}")
        return value

    @field_validator("InternetService")
    @classmethod
    def validate_internet_service(cls, value: str) -> str:
        allowed = {"DSL", "Fiber optic", "No"}
        if value not in allowed:
            raise ValueError(f"Invalid InternetService value '{value}'. Must be one of {allowed}")
        return value

    @field_validator("PaymentMethod")
    @classmethod
    def validate_payment_method(cls, value: str) -> str:
        allowed = {
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        }
        if value not in allowed:
            raise ValueError(f"Invalid PaymentMethod value '{value}'. Must be one of {allowed}")
        return value