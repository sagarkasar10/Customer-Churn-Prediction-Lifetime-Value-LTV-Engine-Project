# System Architecture

## Overview

This document describes the high-level architecture of the Customer Churn Prediction & Lifetime Value (LTV) Engine, explaining how all components connect and interact with each other.
The system is designed to be modular, scalable, and production-ready

---

## High Level Architecture

Raw Data (CSV)
↓
Data Preparation & Feature Engineering
↓
Machine Learning Model Training
↓
Model Artifacts (.pkl files)
↓
FastAPI Application
↓
┌────────────────────┬─────────────────────┐
│ Single Predict │ Batch Predict │
│ /predict/single │ /predict/batch │
└────────────────────┴─────────────────────┘
↓
PostgreSQL Database
↓
Metabase / Superset Dashboard


---

## Component Breakdown

### 1. Data Layer
- Loads raw IBM Telco Customer Churn CSV dataset
- Cleans and preprocesses features
- Encodes categorical variables
- Splits data into train and test sets

### 2. Machine Learning Layer
- Trains baseline and ensemble models
- Calculates LTV using inference engine
- Evaluates model performance
- Exports trained model artifacts

### 3. API Layer
- Serves predictions via REST API endpoints
- Validates input data using Pydantic schemas
- Loads trained models into memory at startup
- Handles single and batch predictions

### 4. Database Layer
- Stores customer prediction results
- Manages database sessions and connections
- Handles CRUD operations
- Manages DDL scripts and indexes

### 5. Dashboard Layer
- Connects to PostgreSQL database
- Displays churn risk and LTV metrics
- Provides interactive business insights
- **Tool:** Metabase / Apache Superset

### 6. DevOps Layer
- Containerizes the entire application
- Manages service networking
- Single command deployment
- **Tool:** Docker, Docker Compose

---

## Data Flow

Customer Data → API Request
↓
Pydantic Schema Validation
↓
Model Loader (loads .pkl from models/)
↓
Inference Engine (LTV Calculation)
↓
Prediction Response
↓
Save to PostgreSQL
↓
Dashboard reads from PostgreSQL


---

## Technology Summary

| Layer | Technology |
|---|---|
| Data Processing | Python, Pandas, NumPy |
| Machine Learning | Scikit-learn |
| API Framework | FastAPI |
| Data Validation | Pydantic |
| Database | PostgreSQL, SQLAlchemy |
| Dashboard | Metabase / Apache Superset |
| Containers | Docker, Docker Compose |
| Testing | Pytest |
| Version Control | Git, GitHub |

