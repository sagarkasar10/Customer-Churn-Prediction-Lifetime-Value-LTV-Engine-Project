# Data Dictionary

## Overview

This document describes all columns, data types, and descriptions for the IBM Telco Customer Churn dataset used in the Customer Churn Prediction & Lifetime Value (LTV) Engine.

---

## Original Dataset Columns

| Column | Data Type | Description |
|---|---|---|
| customerID | String | Unique identifier for each customer |
| gender | String | Customer gender (Male / Female) |
| SeniorCitizen | Integer | Whether the customer is a senior citizen (1 = Yes, 0 = No) |
| Partner | String | Whether the customer has a partner (Yes / No) |
| Dependents | String | Whether the customer has dependents (Yes / No) |
| tenure | Integer | Number of months the customer has been with the company |
| PhoneService | String | Whether the customer has phone service (Yes / No) |
| MultipleLines | String | Whether the customer has multiple lines (Yes / No / No phone service) |
| InternetService | String | Type of internet service (DSL / Fiber optic / No) |
| OnlineSecurity | String | Whether the customer has online security (Yes / No / No internet service) |
| OnlineBackup | String | Whether the customer has online backup (Yes / No / No internet service) |
| DeviceProtection | String | Whether the customer has device protection (Yes / No / No internet service) |
| TechSupport | String | Whether the customer has tech support (Yes / No / No internet service) |
| StreamingTV | String | Whether the customer streams TV (Yes / No / No internet service) |
| StreamingMovies | String | Whether the customer streams movies (Yes / No / No internet service) |
| Contract | String | Type of contract (Month-to-month / One year / Two year) |
| PaperlessBilling | String | Whether the customer uses paperless billing (Yes / No) |
| PaymentMethod | String | Payment method (Electronic check / Mailed check / Bank transfer / Credit card) |
| MonthlyCharges | Float | Monthly charges in USD |
| TotalCharges | Float | Total charges in USD (can contain blank spaces) |
| Churn | String | Whether the customer churned (Yes / No) — Target Variable |

---

## Engineered Columns

| Column | Data Type | Description |
|---|---|---|
| HistoricalRevenue | Float | Calculated as tenure × MonthlyCharges — baseline revenue target |
| Churn | Integer | Encoded from Yes/No to 1/0 for model training |

---

## Preprocessing Steps Applied

| Step | Description |
|---|---|
| TotalCharges cleaning | Blank spaces removed and converted to numeric |
| Missing values | Filled with median value |
| customerID | Dropped — not a predictive feature |
| Categorical encoding | One-hot encoded using pd.get_dummies(drop_first=True) |
| Train/Test Split | 80% training, 20% testing with random_state=42 |

---

## Dataset Statistics

| Metric | Value |
|---|---|
| Total Customers | 7,043 |
| Total Features | 21 |
| Training Samples | 5,634 |
| Test Samples | 1,409 |
| Churn Rate | 26.5% |
| Non-Churn Rate | 73.5% |

---

## Target Variable

| Value | Meaning |
|---|---|
| 0 | Customer did not churn |
| 1 | Customer churned |