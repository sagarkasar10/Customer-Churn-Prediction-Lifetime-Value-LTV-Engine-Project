import os
import pickle

def calculate_ltv(monthly_charges: float, churn_probability: float, baseline_variance: float) -> float:
    """Calculates Lifetime Value based on monthly charge and risk factors."""
    denominator = churn_probability + baseline_variance

    if denominator == 0:
        return 0.0

    ltv = monthly_charges / denominator
    return round(ltv, 2)


def compute_predictive_ltv(client_features: dict, regressor_model=None):
    """Computes churn probability, predictive LTV, and risk tier."""
    monthly_charges = client_features.get("MonthlyCharges", 0.0)

    # Placeholder values until dedicated churn model is linked
    churn_probability = 0.5
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