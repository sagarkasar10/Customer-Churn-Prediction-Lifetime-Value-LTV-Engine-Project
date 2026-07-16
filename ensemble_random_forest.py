import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ---- Load raw data ----
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn (1).csv")

# ---- Prepare data ----
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})
df = df.drop(columns=["customerID"])
df = pd.get_dummies(df, drop_first=True)

X = df.drop(columns=["Churn"])
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---- 1. Basic Random Forest ----
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
print("Baseline Random Forest trained successfully")

