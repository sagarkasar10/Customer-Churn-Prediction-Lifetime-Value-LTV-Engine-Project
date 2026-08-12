import pickle
import sys
sys.path.append("src/ml")
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score
from prepare_data import get_processed_data

# ---- Load data ----
X_train, X_test, y_train, y_test = get_processed_data()

# ---- Load trained models ----
with open("src/ml/baseline_regressor.pkl", "rb") as f:
    baseline_model = pickle.load(f)

with open("src/ml/ensemble_regressor.pkl", "rb") as f:
    ensemble_model = pickle.load(f)

# ---- Baseline model evaluation ----
baseline_features = ["tenure", "MonthlyCharges"]
baseline_preds = baseline_model.predict(X_test[baseline_features])
baseline_mae = mean_absolute_error(y_test, baseline_preds)
baseline_r2 = r2_score(y_test, baseline_preds)

print("=== Baseline Linear Regression ===")
print(f"MAE : {baseline_mae:.4f}")
print(f"R²  : {baseline_r2:.4f}")

# ---- Ensemble model evaluation ----
ensemble_preds = ensemble_model.predict(X_test)
ensemble_mae = mean_absolute_error(y_test, ensemble_preds)
ensemble_r2 = r2_score(y_test, ensemble_preds)

print("\n=== Ensemble Random Forest Regressor ===")
print(f"MAE : {ensemble_mae:.4f}")
print(f"R²  : {ensemble_r2:.4f}")

# ---- Comparison ----
print("\n=== Model Comparison ===")
comparison = pd.DataFrame({
    "Model": ["Baseline LR", "Ensemble RF"],
    "MAE"  : [baseline_mae, ensemble_mae],
    "R2"   : [baseline_r2, ensemble_r2]
})
print(comparison.round(4))