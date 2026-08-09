from typing import List
from pydantic import BaseModel
import asyncio 
from functools import partial
from fastapi import APIRouter, HTTPException, status
router = APIRouter()
from src.backend.crud import create_prediction 
from src.schemas.customer import Customer
from src.ml.model_loader import model_registry
from src.ml.inference_engine import compute_predictive_ltv
import pandas as pd
import numpy as np
import time

class BatchPredictionRequest(BaseModel):
    customers: List[Customer]

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


def _predict_one(customer: Customer) -> dict:
   
    churn_prob, ltv, risk = compute_predictive_ltv(
        client_features=customer.model_dump(),
        classifier_model=model_registry.classifier,
        regressor_model=model_registry.regressor,
        scaler=model_registry.scaler,
    )
    return {
        "customerID": customer.customerID,
        "churn_probability": churn_prob,
        "predicted_ltv": ltv,
        "risk_tier": risk,
    }


@router.post("/predict/batch")
async def predict_batch(request: BatchPredictionRequest):

    # Auto-load models if not yet loaded in registry (mirrors
    # src/routers/single_predict.py's startup-safety check)
    if model_registry.classifier is None:
        model_registry.load_models()

    try:
        predictions = await run_batch(request.customers, _predict_one)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Batch prediction calculation failed: {str(exc)}"
        )


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

