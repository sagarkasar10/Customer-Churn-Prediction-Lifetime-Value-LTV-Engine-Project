import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# ---- Load processed training data ----
train = pd.read_csv("train_processed.csv")
test = pd.read_csv("test_processed.csv")

# ---- Key numeric features only ----
features = ["tenure", "MonthlyCharges", "SeniorCitizen_Yes"]

# Check which features exist
available_features = [f for f in features if f in train.columns]
print("Using features:", available_features)

X_train = train[available_features]
y_train = train["HistoricalRevenue"]

X_test = test[available_features]
y_test = test["HistoricalRevenue"]

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