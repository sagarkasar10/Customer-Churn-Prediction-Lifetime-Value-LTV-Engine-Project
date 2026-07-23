import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix, classification_report
)

def rf_model(X_train, y_train):
    # ---- 1. Basic Random Forest ----
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    print("Baseline Random Forest trained successfully")
    return rf

# ---- 2. Feature importance extraction ----
def feature_importance_plot(rf, X_train):
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

# ---- 3. Evaluation implementation ----
def evaluate_model(model, X_test, y_test, label="Model"):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    metrics = {
        "model": label,
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_prob),
    }
    print(f"\n--- {label} ---")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    return metrics

# ---- 4. Grid search for tuning ----
def tune_rf(X_train, y_train):
    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2"],
    }
    grid_search = GridSearchCV(
        estimator=RandomForestClassifier(random_state=42),
        param_grid=param_grid,
        cv=5,
        scoring="f1",
        n_jobs=-1,
        verbose=1,
    )
    grid_search.fit(X_train, y_train)
    print("\nBest Params:", grid_search.best_params_)
    print("Best CV F1 Score:", grid_search.best_score_)
    return grid_search.best_estimator_



# ---- 5-7. Compare baseline vs tuned ----
def compare_models(baseline_metrics, tuned_metrics):
    comparison = pd.DataFrame([baseline_metrics, tuned_metrics])
    comparison = comparison.set_index("model")
    print("\n=== Baseline vs Tuned RF Comparison ===")
    print(comparison.round(4))
    return comparison

