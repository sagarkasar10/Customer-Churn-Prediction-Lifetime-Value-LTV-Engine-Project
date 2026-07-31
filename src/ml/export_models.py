import os
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from prepare_data import get_processed_data

# ---- Create models directory ----
os.makedirs("models", exist_ok=True)

# ---- Load data ----
X_train, X_test, y_train, y_test = get_processed_data()

# ---- Train and export baseline model ----
print("Training baseline Linear Regression...")
baseline_model = LinearRegression()
baseline_model.fit(X_train[["tenure", "MonthlyCharges"]], y_train)

with open("models/baseline_regressor.pkl", "wb") as f:
    pickle.dump(baseline_model, f)
print("baseline_regressor.pkl saved to models/")

# ---- Train and export ensemble model ----
print("\nTraining ensemble Random Forest Regressor...")
ensemble_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42
)
ensemble_model.fit(X_train, y_train)

with open("models/ensemble_regressor.pkl", "wb") as f:
    pickle.dump(ensemble_model, f)
print("ensemble_regressor.pkl saved to models/")

print("\nAll models exported to models/ directory successfully!")
