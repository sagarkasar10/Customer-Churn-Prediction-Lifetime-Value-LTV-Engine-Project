from typing import List
from pydantic import BaseModel
import asyncio 
from functools import partial
from fastapi import APIRouter
router = APIRouter()
#from src.db.crud import save_prediction 
import pandas as pd
import numpy as np
import time

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




def vectorized_batch_processing(df: pd.DataFrame):
    # Vectorized LTV calculation
    df["predicted_ltv"] = (
        df["MonthlyCharges"] /
        (df["ChurnProbability"] + df["BaselineVariance"])
    )

    # Vectorized Risk Tier
    df["risk_tier"] = np.select(
        [
            df["ChurnProbability"] < 0.3,
            (df["ChurnProbability"] >= 0.3) & (df["ChurnProbability"] < 0.7),
            df["ChurnProbability"] >= 0.7
        ],
        ["Low", "Medium", "High"],
        default="Unknown"
    )

    return df



def benchmark_batch_processing(df: pd.DataFrame):
    start_time = time.perf_counter()

    result = vectorized_batch_processing(df)

    end_time = time.perf_counter()

    print(f"Processed Records: {len(df)}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")

    return result


def api_usage_guide():
    print("\n===== API USAGE GUIDE =====")
    print("Base URL: http://127.0.0.1:8000")
    print("POST /predict/single")
    print("POST /predict/batch")
    print("Swagger Docs: http://127.0.0.1:8000/docs")
    print("\nResponse Fields:")
    print("- predicted_ltv")
    print("- risk_tier")
    print("\nStatus Codes:")
    print("200 - Success")
    print("400 - Bad Request")
    print("422 - Validation Error")
    print("500 - Internal Server Error")

