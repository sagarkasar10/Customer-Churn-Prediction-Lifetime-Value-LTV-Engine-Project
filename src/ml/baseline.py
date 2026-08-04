import os
import pickle
from sklearn.linear_model import LinearRegression
from prepare_data import get_processed_data


def train_baseline():
    print("--- Training Baseline Linear Regression ---")

    # 1. Load split data
    X_train, X_test, y_train, y_test = get_processed_data()

    # 2. Extract baseline features
    baseline_features = ["tenure", "MonthlyCharges", "SeniorCitizen"]
    X_train_sub = X_train[baseline_features]

    # 3. Train model
    baseline_model = LinearRegression()
    baseline_model.fit(X_train_sub, y_train)

    print("Baseline Linear Regression trained successfully")
    print(f"Coefficients: {baseline_model.coef_}")
    print(f"Intercept: {baseline_model.intercept_:.4f}")

    # 4. Pickle artifact
    model_path = os.path.join("ml", "baseline_regressor.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(baseline_model, f)

    print(f"Saved model to: {model_path}\n")


if __name__ == "__main__":
    train_baseline()