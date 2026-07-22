"""
model_loader.py
Loads the trained machine learning model.
"""

import pickle

from backend.config import MODEL_PATH


def load_model():
    #Loads the trained ML model.
    #Returns trained model object.

    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    return model