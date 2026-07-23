from typing import List
from pydantic import BaseModel
import asyncio 
from functools import partial
from fastapi import APIRouter
router = APIRouter()
#from src.db.crud import save_prediction 

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
async def predict_batch(request: BatchPredictionRequest):

    predictions = []

    for customer in request.customers:
        prediction = {
            "customerID": customer.customerID,
            "churn_probability": 0.35,
            "predicted_ltv": 1500.0,
            "risk_tier": "Medium"
        }

        # TODO: SAVE PREDICTION TO DATABASE USING MEMBER 2'S CRUD FUNCTION
        # save_prediction(prediction)  # Save each prediction to the database

        predictions.append(prediction)

    return {
        "message": "Batch prediction completed successfully",
        "total_customers": len(predictions),
        "predictions": predictions
    }