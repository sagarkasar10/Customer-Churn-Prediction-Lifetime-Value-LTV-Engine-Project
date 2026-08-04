"""
model_loader.py
Loads the trained ML model.
"""

import pickle
import logging

from src.backend.config import MODEL_PATH

logger = logging.getLogger(__name__)

model = None

def load_model():
    #Load trained ML model.

    global model

    try:
        with open(MODEL_PATH, "rb") as file:
            model = pickle.load(file)

        logger.info("Model loaded successfully.")

    except Exception as e:
        logger.error(f"Error loading model: {e}")

        model = None

    return model


def get_model():
    #Returns loaded model.
    return model