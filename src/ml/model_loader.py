import os
import joblib
from typing import Optional, Any

class ModelRegistry:
    _instance: Optional["ModelRegistry"] = None

    def __new__(cls) -> "ModelRegistry":
        if cls._instance is None:
            cls._instance = super(ModelRegistry, cls).__new__(cls)
            cls._instance.regressor = None
            cls._instance.classifier = None
            cls._instance.scaler = None
        return cls._instance

    def load_models(self, model_dir: str = "src/ml") -> None:
        """Loads serialized machine learning models into memory cache."""
        ensemble_path = os.path.join(model_dir, "ensemble_regressor.pkl")
        baseline_path = os.path.join(model_dir, "baseline_regressor.pkl")
        classifier_path = os.path.join(model_dir, "churn_classifier.pkl")
        scaler_path = os.path.join(model_dir, "feature_scaler.pkl")

        if os.path.exists(ensemble_path):
            self.regressor = joblib.load(ensemble_path)
            print("Loaded production ensemble regression model.")
        elif os.path.exists(baseline_path):
            self.regressor = joblib.load(baseline_path)
            print("Loaded baseline regression model.")
        else:
            self.regressor = None
            print("Warning: No pre-trained model files found in ml/ directory.")

        if os.path.exists(classifier_path):
            self.classifier = joblib.load(classifier_path)
            print("Loaded churn classifier.")
        else:
            self.classifier = None
            print(f"Warning: no churn classifier found at {classifier_path} — run `python main.py` first.")

        if os.path.exists(scaler_path):
            self.scaler = joblib.load(scaler_path)
            print("Loaded feature scaler.")
        else:
            self.scaler = None
            print(f"Warning: no feature scaler found at {scaler_path} — run `python main.py` first.")

model_registry = ModelRegistry()