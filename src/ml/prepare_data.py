import pandas as pd
from sklearn.model_selection import train_test_split

# ---- Load raw data ----
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn (1).csv")

# ---- Clean TotalCharges space issues ----
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].str.strip(), errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# ---- Calculate baseline historical revenue ----
# Formula: tenure × MonthlyCharges
df["HistoricalRevenue"] = df["tenure"] * df["MonthlyCharges"]

# ---- Drop customerID ----
df = df.drop(columns=["customerID"])

# ---- Encode target ----
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

# ---- Encode categorical columns ----
df = pd.get_dummies(df, drop_first=True)

# ---- Train/test split ----
X = df.drop(columns=["HistoricalRevenue"])
y = df["HistoricalRevenue"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---- Combine and save processed files ----
train_processed = X_train.copy()
train_processed["HistoricalRevenue"] = y_train.values

test_processed = X_test.copy()
test_processed["HistoricalRevenue"] = y_test.values

train_processed.to_csv("train_processed.csv", index=False)
test_processed.to_csv("test_processed.csv", index=False)

print("Data preparation complete!")
print(f"Train shape: {train_processed.shape}")
print(f"Test shape: {test_processed.shape}")
print(f"\nSample HistoricalRevenue values:")
print(train_processed["HistoricalRevenue"].describe())