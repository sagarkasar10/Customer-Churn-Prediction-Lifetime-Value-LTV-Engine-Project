import pandas as pd
import numpy as np

# Load the existing dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn (1).csv")

# Create 100 mock records by sampling existing data
mock_data = df.sample(n=100, replace=True).copy()

# Exclude binary columns from modification
exclude_cols = ["SeniorCitizen"]

# Select only numeric columns except excluded ones
numeric_cols = [
    col for col in mock_data.select_dtypes(include=np.number).columns
    if col not in exclude_cols
]

# Add slight random noise to numeric columns
for col in numeric_cols:
    std = mock_data[col].std()
    if pd.notna(std) and std > 0:
        noise = np.random.normal(0, std * 0.05, len(mock_data))
        mock_data[col] = mock_data[col] + noise

# Save the generated mock dataset
mock_data.to_csv("mock_dataset.csv", index=False)

print("Mock dataset generated successfully!")
print(mock_data.head())