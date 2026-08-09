import os
import pandas as pd
from sqlalchemy import create_engine, text
from sklearn.model_selection import train_test_split

# Get path relative to the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "WA_Fn-UseC_-Telco-Customer-Churn (1).csv")

def process_raw_data(file_path=DATA_PATH):
    """Processes raw data, creates HistoricalRevenue target, and saves train/test splits."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset non-existent at path: {file_path}.\n"
            "Please ensure 'WA_Fn-UseC_-Telco-Customer-Churn (1).csv' is inside your main project root directory."
        )

    print(f"--- Processing raw data from: {file_path} ---")
    df = pd.read_csv(file_path)

    # Handle missing/space values in TotalCharges
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].str.strip(), errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

    # 1. Database Connection URL
    DB_URL = "postgresql://postgres:postTiya@localhost:5432/customer_churn"

    # 3. Connect and bulk upload to PostgreSQL
    engine = create_engine(DB_URL)

    with engine.begin() as conn:
        conn.execute(text('ALTER TABLE customers ADD COLUMN IF NOT EXISTS "Churn" VARCHAR(10);'))
    
    print("Uploading data to PostgreSQL database...")
    # 'append' pushes all rows into the existing 'customers' table without deleting structure
    df.to_sql('customers', con=engine, if_exists='append', index=False)
    
    print(f"SUCCESS: Uploaded {len(df)} rows into the 'customers' table!")

    # Target variable calculation
    df["HistoricalRevenue"] = df["tenure"] * df["MonthlyCharges"]

    # Drop non-predictive columns
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    # Encode target variable
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

    # One-hot encoding for categorical variables
    df = pd.get_dummies(df, drop_first=True)

    # Train / Test split
    X = df.drop(columns=["HistoricalRevenue"])
    y = df["HistoricalRevenue"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Save outputs to project root for models & backend to access
    train_path = os.path.join(BASE_DIR, "train_processed.csv")
    test_path = os.path.join(BASE_DIR, "test_processed.csv")

    train_processed = X_train.copy()
    train_processed["HistoricalRevenue"] = y_train.values

    test_processed = X_test.copy()
    test_processed["HistoricalRevenue"] = y_test.values

    train_processed.to_csv(train_path, index=False)
    test_processed.to_csv(test_path, index=False)

    print("Data processing complete! Saved train_processed.csv & test_processed.csv\n")
    return X_train, X_test, y_train, y_test


def get_processed_data():
    """Loads pre-processed CSVs or triggers data processing if missing."""
    train_path = os.path.join(BASE_DIR, "train_processed.csv")
    test_path = os.path.join(BASE_DIR, "test_processed.csv")

    if os.path.exists(train_path) and os.path.exists(test_path):
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        X_train = train_df.drop(columns=["HistoricalRevenue"])
        y_train = train_df["HistoricalRevenue"]

        X_test = test_df.drop(columns=["HistoricalRevenue"])
        y_test = test_df["HistoricalRevenue"]

        return X_train, X_test, y_train, y_test
    else:
        return process_raw_data()


if __name__ == "__main__":
    process_raw_data()