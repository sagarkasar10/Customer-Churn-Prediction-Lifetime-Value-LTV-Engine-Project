import os
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Preprocessing import preprocessing_data
from feature_services import (
    handle_missing_service_data,
    total_services_count,
    service_complexity_score,
    create_tenure_cohorts,
    create_average_monthly_ratio,
    handle_outliers
)


def test_integration():

    print("Loading mock dataset...")

    df = pd.read_csv("mock_dataset.csv")

    # ----------------------------
    # Preprocessing
    # ----------------------------
    print("Running preprocessing...")

    df = preprocessing_data(df)

    # ----------------------------
    # Feature Engineering
    # ----------------------------
    print("Running feature engineering...")

    df = handle_missing_service_data(df)
    df = total_services_count(df)
    df = service_complexity_score(df)
    df = create_tenure_cohorts(df)
    df = create_average_monthly_ratio(df)
    df = handle_outliers(df)

    # ----------------------------
    # Encode Target
    # ----------------------------
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({
            "Yes": 1,
            "No": 0
        })

    # ----------------------------
    # One Hot Encoding
    # ----------------------------
    categorical_cols = [
        col for col in df.select_dtypes(include=["object","string", "category"]).columns
        if col not in ["customerID", "Churn"]
    ]

    clean_df = pd.get_dummies(
        df,
        columns=categorical_cols,
        drop_first=True
    )

    # ----------------------------
    # Prepare Features
    # ----------------------------
    X = clean_df.drop(
        columns=["customerID", "Churn"],
        errors="ignore"
    )

    # ----------------------------
    # Scale Numerical Columns
    # ----------------------------
    numerical_columns = [
        col
        for col in [
            "tenure",
            "MonthlyCharges",
            "TotalCharges"
        ]
        if col in X.columns
    ]

    scaler = StandardScaler()

    X[numerical_columns] = scaler.fit_transform(
        X[numerical_columns]
    )

    # ----------------------------
    # Load Model
    # ----------------------------
    model_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "best_logistic_regression_model.pkl"
    )

    model = joblib.load(model_path)

    # ----------------------------
    # Match Training Columns
    # ----------------------------
    expected_columns = model.feature_names_in_

    X = X.reindex(
        columns=expected_columns,
        fill_value=0
    )

    # ----------------------------
    # Prediction
    # ----------------------------
    predictions = model.predict(X)

    print("\nPredictions")
    print(predictions)

    print("\nNumber of predictions:", len(predictions))

    print("\nIntegration Test Passed Successfully!")


if __name__ == "__main__":
    test_integration()