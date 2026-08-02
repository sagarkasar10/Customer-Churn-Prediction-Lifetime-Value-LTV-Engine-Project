# Modeling Documentation

## Overview
This document covers the ML modeling decisions, baseline comparisons, mathematical formulas, and feature importance for the Customer Churn Prediction & Lifetime Value (LTV) Engine Project.

---

## 1. Model Choices

### Baseline Model — Linear Regression
- **File:** `src/ml/train_baseline.py`
- **Why:** Simple, interpretable starting point to establish baseline performance.
- **Features used:** `tenure`, `MonthlyCharges`
- **Target:** `HistoricalRevenue` (tenure × MonthlyCharges)

### Ensemble Model — Random Forest Regressor
- **File:** `src/ml/train_ensemble.py`
- **Why:** Captures non-linear relationships between features that Linear Regression misses.
- **Features used:** All processed features
- **Target:** `HistoricalRevenue`

---

## 2. Mathematical Formulas

### Historical Revenue (Target Variable)
$$\text{HistoricalRevenue} = \text{tenure} \times \text{MonthlyCharges}$$

### LTV Calculation
$$\text{LTV} = \frac{\text{MonthlyCharges}}{\text{ChurnProbability} + \text{BaselineVariance}}$$

---

## 3. Baseline Comparison

| Model | MAE | R² |
|---|---|---|
| Linear Regression (Baseline) | — | — |
| Random Forest Regressor (Ensemble) | — | — |

*(Fill in values after running `src/ml/evaluate.py`)*

---

## 4. Feature Importance

Top features identified by the Random Forest Regressor:

| Rank | Feature | Importance |
|---|---|---|
| 1 | tenure | High |
| 2 | MonthlyCharges | High |
| 3 | TotalCharges | Medium |
| 4 | Contract type | Medium |
| 5 | InternetService | Low |

---

## 5. Data Preparation
- **File:** `src/ml/prepare_data.py`
- Raw CSV loaded and cleaned
- `TotalCharges` spaces fixed and converted to numeric
- `customerID` dropped
- `Churn` encoded as 0/1
- Categorical columns one-hot encoded via `pd.get_dummies`
- 80/20 train/test split with `random_state=42`

---

## 6. Pipeline Serialization
- **File:** `src/ml/export_models.py`
- Both models exported as `.pkl` files to `models/` directory
- `models/baseline_regressor.pkl`
- `models/ensemble_regressor.pkl`