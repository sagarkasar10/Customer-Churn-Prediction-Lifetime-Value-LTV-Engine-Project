# Model Cards

## Overview

This document provides detailed information about each machine learning model used in the Customer Churn Prediction & Lifetime Value (LTV) Engine, including model details, performance metrics, and limitations.

---

## Model 1 — Logistic Regression (Churn Classifier)

### Model Details
| Field | Details |
|---|---|
| Model Type | Logistic Regression |
| Task | Binary Classification (Churn / No Churn) |
| File | `model_logreg.py` |
| Framework | Scikit-learn |
| Random State | 42 |

### Input Features
| Feature | Type |
|---|---|
| tenure | Numeric |
| MonthlyCharges | Numeric |
| TotalCharges | Numeric |
| Contract | Categorical (encoded) |
| InternetService | Categorical (encoded) |
| PaymentMethod | Categorical (encoded) |

### Output
| Field | Description |
|---|---|
| churn_probability | Probability of customer churning (0 to 1) |
| prediction | 0 = No Churn, 1 = Churn |

### Performance Metrics
| Metric | Value |
|---|---|
| Accuracy | — |
| Precision | — |
| Recall | — |
| F1 Score | — |
| ROC AUC | — |


### Limitations
- Assumes linear relationship between features and churn
- May underperform on highly imbalanced data
- Does not capture complex non-linear patterns

---

## Model 2 — Random Forest Classifier (Ensemble Churn)

### Model Details
| Field | Details |
|---|---|
| Model Type | Random Forest Classifier |
| Task | Binary Classification (Churn / No Churn) |
| File | `ensemble_random_forest.py` |
| Framework | Scikit-learn |
| Random State | 42 |
| n_estimators | 100 |
| max_depth | None |

### Input Features
- All processed and encoded features from the dataset

### Output
| Field | Description |
|---|---|
| churn_probability | Probability of customer churning (0 to 1) |
| prediction | 0 = No Churn, 1 = Churn |

### Performance Metrics
| Metric | Value |
|---|---|
| Accuracy | — |
| Precision | — |
| Recall | — |
| F1 Score | — |
| ROC AUC | — |


### Limitations
- Slower to train compared to Logistic Regression
- Less interpretable than linear models
- May overfit on small datasets

---

## Model 3 — XGBoost Classifier

### Model Details
| Field | Details |
|---|---|
| Model Type | XGBoost Classifier |
| Task | Binary Classification (Churn / No Churn) |
| File | `xgb_model.py` |
| Framework | XGBoost |
| Random State | 42 |

### Input Features
- All processed and encoded features from the dataset

### Output
| Field | Description |
|---|---|
| churn_probability | Probability of customer churning (0 to 1) |
| prediction | 0 = No Churn, 1 = Churn |

### Performance Metrics
| Metric | Value |
|---|---|
| Accuracy | — |
| Precision | — |
| Recall | — |
| F1 Score | — |
| ROC AUC | — |


### Limitations
- Requires careful hyperparameter tuning
- More complex to interpret than simpler models
- Computationally expensive for large datasets

---

## Model 4 — Linear Regression (Baseline LTV)

### Model Details
| Field | Details |
|---|---|
| Model Type | Linear Regression |
| Task | Regression (Historical Revenue Prediction) |
| File | `src/ml/train_baseline.py` |
| Framework | Scikit-learn |
| Random State | 42 |

### Input Features
| Feature | Type |
|---|---|
| tenure | Numeric |
| MonthlyCharges | Numeric |

### Output
| Field | Description |
|---|---|
| HistoricalRevenue | Predicted historical revenue in USD |

### Performance Metrics
| Metric | Value |
|---|---|
| MAE | — |
| R² | — |


### Limitations
- Only uses two features
- Assumes linear relationship between features and revenue
- Cannot capture complex customer behavior patterns

---

## Model 5 — Random Forest Regressor (Ensemble LTV)

### Model Details
| Field | Details |
|---|---|
| Model Type | Random Forest Regressor |
| Task | Regression (Historical Revenue Prediction) |
| File | `src/ml/train_ensemble.py` |
| Framework | Scikit-learn |
| Random State | 42 |
| n_estimators | 100 |
| max_depth | 10 |

### Input Features
- All processed and encoded features from the dataset

### Output
| Field | Description |
|---|---|
| HistoricalRevenue | Predicted historical revenue in USD |

### Performance Metrics
| Metric | Value |
|---|---|
| MAE | — |
| R² | — |


### Limitations
- Slower than baseline Linear Regression
- May overfit without proper tuning
- Memory intensive for large datasets