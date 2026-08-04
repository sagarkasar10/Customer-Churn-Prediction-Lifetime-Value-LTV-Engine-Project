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
        return cls._instance

    def load_models(self, model_dir: str = "ml") -> None:
        """Loads serialized machine learning models into memory cache."""
        ensemble_path = os.path.join(model_dir, "ensemble_regressor.pkl")
        baseline_path = os.path.join(model_dir, "baseline_regressor.pkl")

        if os.path.exists(ensemble_path):
            self.regressor = joblib.load(ensemble_path)
            print("Loaded production ensemble regression model.")
        elif os.path.exists(baseline_path):
            self.regressor = joblib.load(baseline_path)
            print("Loaded baseline regression model.")
        else:
            self.regressor = None
            print("Warning: No pre-trained model files found in ml/ directory.")

model_registry = ModelRegistry()