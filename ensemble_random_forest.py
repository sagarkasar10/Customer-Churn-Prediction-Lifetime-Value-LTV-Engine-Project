import pandas as pd
import matplotlib.pyplot as plt
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



# ---- 2. Feature importance extraction ----
importances = pd.Series(rf.feature_importances_, index=X_train.columns)
importances = importances.sort_values(ascending=False)


print("\nTop 10 Important Features:")
print(importances.head(10))

plt.figure(figsize=(8, 6))
importances.head(15).sort_values().plot(kind="barh")
plt.title("Random Forest - Top Feature Importances")
plt.xlabel("Importance")
plt.tight_layout()
plt.show()