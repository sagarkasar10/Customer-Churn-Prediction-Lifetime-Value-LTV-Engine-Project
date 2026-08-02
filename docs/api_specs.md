```markdown
# API Specifications

## Overview

This document defines the REST API endpoints for the Customer Churn Prediction & Lifetime Value (LTV) Engine. The API is built using FastAPI and exposes endpoints for single and batch customer predictions.

---

## Base URL
```

http://localhost:8000

```

---

## Authentication

Currently no authentication is required. Future versions will support API key authentication.

---

## Endpoints

### 1. Health Check
```

GET /

```

**Description:** Check if the API is running.

**Response:**
```json
{
  "status": "ok",
  "message": "Customer Churn Prediction API is running"
}
```

---

### 2. Single Customer Prediction
```

POST /predict/single

```

**Description:** Predict churn probability and LTV for a single customer.

**Request Body:**
```json
{
  "tenure": 12,
  "MonthlyCharges": 65.5,
  "TotalCharges": 786.0,
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check"
}
```

**Response:**
```json
{
  "churn_probability": 0.73,
  "predicted_ltv": 89.72,
  "risk_tier": "High"
}
```

**Status Codes:**
| Code | Meaning |
|---|---|
| 200 | Prediction successful |
| 422 | Validation error — invalid input |
| 500 | Internal server error |

---

### 3. Batch Customer Prediction
```

POST /predict/batch

```

**Description:** Predict churn probability and LTV for multiple customers at once.

**Request Body:**
```json
{
  "customers": [
    {
      "tenure": 12,
      "MonthlyCharges": 65.5,
      "Contract": "Month-to-month"
    },
    {
      "tenure": 36,
      "MonthlyCharges": 45.0,
      "Contract": "One year"
    }
  ]
}
```

**Response:**
```json
{
  "results": [
    {
      "churn_probability": 0.73,
      "predicted_ltv": 89.72,
      "risk_tier": "High"
    },
    {
      "churn_probability": 0.21,
      "predicted_ltv": 214.28,
      "risk_tier": "Low"
    }
  ],
  "total_customers": 2
}
```

**Status Codes:**
| Code | Meaning |
|---|---|
| 200 | Batch prediction successful |
| 422 | Validation error — invalid input |
| 500 | Internal server error |

---

## Risk Tier Classification

| Risk Tier | Churn Probability |
|---|---|
| Low | 0.0 — 0.3 |
| Medium | 0.3 — 0.6 |
| High | 0.6 — 1.0 |

---

## Error Response Format

```json
{
  "detail": "Error message describing what went wrong"
}
```

---

## Notes

- All requests must include `Content-Type: application/json` header
- Batch endpoint accepts a maximum of 1000 customers per request
- LTV is calculated using the formula: `MonthlyCharges / (ChurnProbability + BaselineVariance)`
```

