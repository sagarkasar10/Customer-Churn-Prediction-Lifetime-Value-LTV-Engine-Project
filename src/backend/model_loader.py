"""Loads the trained machine learning model."""

import joblib
from pathlib import Path

from backend.config import MODEL_PATH


def load_model():

    #Load the trained ML model
    model_path = Path(MODEL_PATH)

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found at: {MODEL_PATH}"
        )

    model = joblib.load(model_path)

    return model