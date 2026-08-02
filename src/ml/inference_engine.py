import pickle

# ---- Load trained models ---
with open("baseline_regressor.pkl", "rb") as f:
    baseline_model = pickle.load(f)

with open("ensemble_regressor.pkl", "rb") as f:
    ensemble_model = pickle.load(f)

# ---- LTV Calculation Function ----
def calculate_ltv(monthly_charges, churn_probability, baseline_variance):
    
    denominator = churn_probability + baseline_variance

    if denominator == 0:
        return 0.0

    ltv = monthly_charges / denominator
    return round(ltv, 2)

print("Inference engine loaded successfully")
print("calculate_ltv() function is ready to use")