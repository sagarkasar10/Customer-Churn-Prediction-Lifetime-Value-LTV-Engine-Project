from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.routers import single_predict
from src.ml.model_loader import model_registry

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Load ML models into memory cache
    print("Application booting: Initializing model weights...")
    model_registry.load_models()
    yield
    # Shutdown: Clean up resources if necessary
    print("Application shutting down...")

app = FastAPI(
    title="Customer Churn & LTV Prediction Engine",
    description="Predictive API service for high-risk customer retention and LTV prioritization.",
    version="1.0.0",
    lifespan=lifespan
)

# Register single prediction router
app.include_router(single_predict.router)

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {
        "status": "healthy",
        "models_loaded": model_registry.regressor is not None
    }