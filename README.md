# Customer-Churn-Prediction-Lifetime-Value-LTV-Engine-Project

## 1. Project Overview
Predicts which customers are at risk of churning and estimates each
customer's predictive Lifetime Value (LTV), so retention campaigns
can be prioritized by expected revenue impact.

## 2. Week 1 – Data Ingestion & EDA

### Data Source
### Data Preprocessing
### Exploratory Data Analysis
### Key EDA Findings
### Baseline Analytics

## 3. Week 2 – Feature Engineering & Predictive Modeling

### Feature Engineering
### Logistic Regression
### Random Forest
### XGBoost
### Model Evaluation
### SHAP Explainability

## Running the training pipeline

```bash
pip install -r requirements.txt
python main.py
```

This runs EDA, cleans and feature-engineers the data, trains and
evaluates Logistic Regression / Random Forest / XGBoost classifiers
plus SHAP explainability, trains the baseline and ensemble LTV
regressors.

## Running the API

```bash
uvicorn src.api.main:app --reload
```

Then see `http://127.0.0.1:8000/docs` for interactive API docs, or
`docs/api_specs.md`.

