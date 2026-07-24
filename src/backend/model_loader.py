"""
model_loader.py
Loads the trained ML model.
"""

import pickle
from backend.config import MODEL_PATH

model = None

def load_model():
    #Load trained ML model.

    global model

    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    return model


def get_model():
    #Returns loaded model.
    return model