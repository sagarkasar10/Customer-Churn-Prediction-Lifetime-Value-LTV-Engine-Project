import pandas as pd
import numpy as np
import xgboost as xgb
import shap 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import standardscaler

# Load the dataset
def load_and_split_data(file_path):
    df = pd.read_csv(file_path)
    
    # Separate features and target variable
    x = df.drop(columns=['customerID', 'Churn'])
    y = df['Churn']

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

    print(f"Data loaded successfully!")
    print(f"Training set shape: {x_train.shape}, Testing set shape: {x_test.shape}")

    return x_train, x_test, y_train, y_test

if __name__ == "__main__":
    file_path = r"G:\WA_Fn-UseC_-Telco-Customer-Churn (1).csv"
    x_train, x_test, y_train, y_test = load_and_split_data(file_path)
    



