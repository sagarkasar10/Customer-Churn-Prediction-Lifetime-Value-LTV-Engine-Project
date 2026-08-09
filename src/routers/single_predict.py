from fastapi import APIRouter, HTTPException, status
from src.schemas.customer import Customer
from src.schemas.predictions import SinglePredictionOutput
from src.ml.model_loader import model_registry
from src.ml.inference_engine import compute_predictive_ltv

router = APIRouter(prefix="/predict", tags=["Predictions"])

@router.post(
    "/single",
    response_model=SinglePredictionOutput,
    status_code=status.HTTP_200_OK,
    summary="Predict Churn & LTV for a Single Customer",
    description="""
    Ingests a single customer profile (demographics, contracted services, and billing history)
    and returns:
    - **Churn Probability**: Real-time likelihood score of cancellation (0.0 - 1.0)
    - **Predicted LTV**: Expected future revenue contribution ($)
    - **Risk Tier**: Classification category (`Low`, `Medium`, or `High`) for targeted retention campaigns.
    """,
    responses={
        200: {
            "description": "Prediction successfully generated.",
            "content": {
                "application/json": {
                    "example": {
                        "customerID": "7590-VHVEG",
                        "churn_probability": 0.6421,
                        "predicted_ltv": 542.75,
                        "risk_tier": "High"
                    }
                }
            }
        },
        422: {"description": "Unprocessable Entity — Input schema validation failed."},
        500: {"description": "Internal Server Error — Prediction model inference failure."}
    }
)
def predict_single(payload: Customer):
    # Auto-load models if not yet loaded in registry
    if model_registry.regressor is None:
        model_registry.load_models()

    customer_dict = payload.model_dump()
    
    try:
        churn_prob, ltv, risk = compute_predictive_ltv(
            client_features=customer_dict,
            classifier_model=model_registry.classifier,
            regressor_model=model_registry.regressor,
            scaler=model_registry.scaler
        )
        return SinglePredictionOutput(
            customerID=payload.customerID,
            churn_probability=churn_prob,
            predicted_ltv=ltv,
            risk_tier=risk
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Single prediction calculation failed: {str(exc)}"
        )