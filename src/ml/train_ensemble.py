import pandas as pd
import pickle
import sys
sys.path.append("src/ml")
from sklearn.ensemble import RandomForestRegressor
from prepare_data import get_processed_data

# ---- Load data from central function ----
X_train, X_test, y_train, y_test = get_processed_data()

# ---- Train ensemble regressor ----
ensemble_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42
)
ensemble_model.fit(X_train, y_train)

print("Ensemble Random Forest Regressor trained successfully")
print(f"Train score (R²): {ensemble_model.score(X_train, y_train):.4f}")
print(f"Test score (R²): {ensemble_model.score(X_test, y_test):.4f}")

# ---- Save model ----
with open("ensemble_regressor.pkl", "wb") as f:
    pickle.dump(ensemble_model, f)

print("\nensemble_regressor.pkl saved successfully")