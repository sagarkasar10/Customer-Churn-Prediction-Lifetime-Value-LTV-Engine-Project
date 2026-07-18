import pandas as pd
import numpy as np
import xgboost as xgb
import shap 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score

# Load the dataset
def load_and_split_data(file_path):
    df = pd.read_csv(file_path)
    
    # Separate features and target variable
    df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

    x = df.drop(columns=['customerID', 'Churn'])
    y = df['Churn']

    # 5. Convert all remaining text columns into numeric 0 and 1 flags
    x = pd.get_dummies(x, drop_first=True)

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

    print(f"Data loaded successfully!")
    print(f"Training set shape: {x_train.shape}, Testing set shape: {x_test.shape}")

    return x_train, x_test, y_train, y_test

def train_xgboost_model(x_train, y_train):
    # Initialize the XGBoost classifier
    xgb_model = xgb.XGBClassifier(eval_metric='logloss', random_state=42)

    # Train the model
    xgb_model.fit(x_train, y_train)

    print("Model trained successfully!")

    return xgb_model


def tuning_and_evaluation_xgb_model(x_test, y_test, xgb_model):
    # Make predictions
    y_pred = xgb_model.predict(x_test)

    # Evaluate the model
    print("Classification Report of XGBoost Model:")
    print(classification_report(y_test, y_pred))

    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"XGBoost Precision: {precision:.4f} \nXGBoost Recall: {recall:.4f} \nXGBoost F1 Score: {f1:.4f}")

def initialize_shap(xgb_model, x_train):
    # Initialize SHAP explainer
    print("Initializing SHAP tree explainer and calculating SHAP values...")
    explainer = shap.TreeExplainer(xgb_model)
    shap_values = explainer.shap_values(x_train)

    return explainer, shap_values




if __name__ == "__main__":
    file_path = "WA_Fn-UseC_-Telco-Customer-Churn (1).csv"

    # 1. Load data
    x_train, x_test, y_train, y_test = load_and_split_data(file_path)

    # 2. Train the model (this holds your actual trained XGBoost object)
    xgboost_model = train_xgboost_model(x_train, y_train)

    # 3. Evaluate the model 
    tuning_and_evaluation_xgb_model(x_test, y_test, xgboost_model)

    # 4. Pass the actual trained model 'xgboost_model' into SHAP
    explainer, shap_values = initialize_shap(xgboost_model, x_train)







