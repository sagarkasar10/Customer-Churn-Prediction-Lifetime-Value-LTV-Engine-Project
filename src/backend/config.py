"""
config.py
Stores configuration variables used throughout the backend.
"""

# Application Configuration
APP_NAME = "Customer Churn Prediction & LTV Engine"
APP_VERSION = "1.0.0"

#PostgresSQL Database
DATABASE_URL = (
    "postgresql://postgres:postTiya@localhost:5432/customer_churn"
)

# ML Model
MODEL_PATH = "src/ml/ensemble_regressor.pkl"