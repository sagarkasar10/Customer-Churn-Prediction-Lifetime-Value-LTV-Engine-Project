# Project Overview

## About the Project

The **Customer Churn Prediction & Lifetime Value (LTV) Engine** is a machine learning system designed to help telecom companies identify customers who are likely to churn and estimate their predicted Lifetime Value (LTV). The system combines machine learning models, REST APIs, database integration, and interactive dashboards to provide actionable business insights.

---

## What the System Does

- Predicts whether a customer is likely to churn (Yes/No)
- Calculates the predicted **Lifetime Value (LTV)** for each customer
- Exposes predictions through a **REST API**
- Stores customer predictions in a **PostgreSQL database**
- Visualizes business insights using an interactive dashboard
- Supports deployment using Docker containers

---

# Tech Stack

| Layer | Technology |
|--------|------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| ML Models | Logistic Regression, Random Forest, Linear Regression |
| API Framework | FastAPI |
| Data Validation | Pydantic |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Dashboard | Metabase / Apache Superset |
| Testing | Pytest |
| DevOps | Docker, Docker Compose |
| Documentation | Markdown, VS Code |
| Version Control | Git & GitHub |

---

# Dataset

**Dataset Name:** IBM Telco Customer Churn Dataset

**Source:** IBM Sample Dataset

**Dataset Statistics**

- Total Customers: **7,043**
- Total Features: **21**
- Target Variable: **Churn (Yes/No)**

The dataset contains customer demographic information, subscription details, billing information, tenure, and churn status.

---


# System Workflow

1. Load customer dataset.
2. Perform data preprocessing and feature engineering.
3. Train machine learning models.
4. Predict customer churn probability.
5. Calculate customer Lifetime Value (LTV).
6. Store prediction results in PostgreSQL.
7. Expose prediction APIs using FastAPI.
8. Visualize insights using dashboards.

---

# Key Formulas

## Historical Revenue

\[
\text{HistoricalRevenue} = \text{Tenure} \times \text{MonthlyCharges}
\]

## Lifetime Value (LTV)

\[
\text{LTV} = \frac{\text{MonthlyCharges}}{\text{ChurnProbability} + \text{BaselineVariance}}
\]

---

# Project Objectives

- Build an end-to-end machine learning solution for customer churn prediction.
- Estimate customer Lifetime Value using churn probability.
- Develop scalable REST APIs for predictions.
- Store prediction results in a relational database.
- Create dashboards for business decision-making.
- Maintain clean documentation and modular project architecture.

---

# Expected Outcomes

After completing the project, the system will be able to:

- Predict customer churn with trained ML models.
- Estimate customer Lifetime Value.
- Serve predictions through FastAPI endpoints.
- Store predictions in PostgreSQL.
- Display business insights on dashboards.
- Support deployment using Docker containers.

---

# Documentation

This document provides a high-level overview of the Customer Churn Prediction & Lifetime Value Engine, including its objectives, architecture, technology stack, workflow, and overall project organization.