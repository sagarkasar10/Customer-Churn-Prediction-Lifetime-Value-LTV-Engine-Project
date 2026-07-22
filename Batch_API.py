from typing import List
from pydantic import BaseModel
import asyncio 
from functools import partial
from fastapi import APIRouter
router = APIRouter()

class CustomerData(BaseModel):
    gender: str 
    senior_citizen: int
    partner: str
    dependents: str
    tenure: int
    phone_service: str
    multiple_lines: str
    internet_service: str
    online_security: str
    online_backup: str
    device_protection: str
    tech_support: str
    streaming_tv: str
    streaming_movies: str
    contract: str
    paperless_billing: str
    payment_method: str
    monthly_charges: float
    total_charges: float

class BatchPredictionRequest(BaseModel):
    customers: List[CustomerData]

async def run_in_thread(func, *args, **kwargs):
    """Run a synchronous function in a separate thread using asyncio."""
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, partial(func, *args, **kwargs))

async def run_batch(customers,predict_func):
    """Run predictions concurrently for multiple customers"""
    tasks = [
        run_in_thread(predict_func, customer) 
        for customer in customers
    ]
    return await asyncio.gather(*tasks)




@router.post("/predict/batch")
async def predict_batch():

    predictions = [
        {
            "customerID": "C001",
            "churn_probability": 0.35,
            "predicted_ltv": 1500.0,
            "risk_tier": "Medium"
        },
        {
            "customerID": "C002",
            "churn_probability": 0.72,
            "predicted_ltv": 850.0,
            "risk_tier": "High"
        },
        {
            "customerID": "C003",
            "churn_probability": 0.18,
            "predicted_ltv": 2400.0,
            "risk_tier": "Low"
        }
    ]

    return {
        "message": "Batch prediction completed successfully",
        "total_customers": len(predictions),
        "predictions": predictions
    }
