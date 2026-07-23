import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# ---- Train baseline Linear Regression ----
baseline_model = LinearRegression()
baseline_model.fit(X_train, y_train)

print("Baseline Linear Regression trained successfully")
print(f"Coefficients: {baseline_model.coef_}")
print(f"Intercept: {baseline_model.intercept_}")

# ---- Save model ----
with open("baseline_regressor.pkl", "wb") as f:
    pickle.dump(baseline_model, f)

print("\nbaseline_regressor.pkl saved successfully")