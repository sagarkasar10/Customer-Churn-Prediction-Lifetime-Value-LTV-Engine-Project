from pydantic import BaseModel, Field

class SinglePredictionOutput(BaseModel):
    customerID: str = Field(..., description="Unique ID of the customer evaluated", examples=["7590-VHVEG"])
    churn_probability: float = Field(..., description="Model probability score for churn risk (0.0 to 1.0)", examples=[0.6421])
    predicted_ltv: float = Field(..., description="Projected dynamic Customer Lifetime Value in currency", examples=[542.75])
    risk_tier: str = Field(..., description="Assigned risk bucket (Low, Medium, High)", examples=["High"])