import pandas as pd

from feature_services import (
    handle_missing_service_data,
    total_services_count,
    service_complexity_score,
    create_tenure_cohorts,
    create_average_monthly_ratio,
)


def calculate_ltv(monthly_charges: float, churn_probability: float, baseline_variance: float) -> float:
    """Calculates Lifetime Value based on monthly charge and risk factors."""
    denominator = churn_probability + baseline_variance

    if denominator == 0:
        return 0.0

    ltv = monthly_charges / denominator
    return round(ltv, 2)


def _build_feature_row(client_features: dict) -> pd.DataFrame:
    """
    Turns one raw customer dict into a single-row, feature-engineered,
    one-hot-encoded DataFrame.
    """
    row = pd.DataFrame([client_features])

    row = handle_missing_service_data(row)
    row = total_services_count(row)
    row = service_complexity_score(row)
    row = create_tenure_cohorts(row)
    row = create_average_monthly_ratio(row)

    categorical_cols = [
        col for col in row.select_dtypes(include=["object", "category"]).columns
        if col not in ("customerID", "Churn")
    ]
    row = pd.get_dummies(row, columns=categorical_cols, drop_first=True)

    return row


def compute_predictive_ltv(client_features: dict, classifier_model, regressor_model=None, scaler=None):
    """Computes churn probability, predictive LTV, and risk tier."""

    if classifier_model is None:
        raise RuntimeError(
            "No churn classifier is loaded. Run `python main.py` to train and "
            "export src/ml/churn_classifier.pkl, then restart the API."
        )

    monthly_charges = client_features.get("MonthlyCharges", 0.0)

    row = _build_feature_row(client_features)
    aligned = row.reindex(columns=classifier_model.feature_names_in_, fill_value=0)
    
    if scaler is not None:
            numeric_cols = [c for c in scaler.feature_names_in_ if c in aligned.columns]
            aligned[numeric_cols] = scaler.transform(aligned[numeric_cols])
    
    churn_probability = float(classifier_model.predict_proba(aligned)[:, 1][0])
    baseline_variance = 0.1

    predicted_ltv = calculate_ltv(
        monthly_charges,
        churn_probability,
        baseline_variance
    )

    risk = (
        "High" if churn_probability > 0.7
        else "Medium" if churn_probability > 0.4
        else "Low"
    )

    return churn_probability, predicted_ltv, risk


if __name__ == "__main__":
    print("Inference engine loaded successfully")
    print("calculate_ltv() function is ready to use")