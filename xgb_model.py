import xgboost as xgb
import shap 
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score, roc_auc_score, accuracy_score


def train_xgboost_model(x_train, y_train):
    # Initialize the XGBoost classifier
    xgb_model = xgb.XGBClassifier(eval_metric='logloss', random_state=42)

    # Train the model
    xgb_model.fit(x_train, y_train)

    print("XGBoost Model trained successfully!")

    return xgb_model


def evaluation_xgb_model(x_test, y_test, xgb_model):
    # Make predictions
    y_pred = xgb_model.predict(x_test)

    # Evaluate the model
    print("Classification Report of XGBoost Model:")
    print(classification_report(y_test, y_pred))

    accuracy = accuracy_score(y_test, y_pred)
    print(f"XGBoost Accuracy: {accuracy:.4f}")

    precision = precision_score(y_test, y_pred)
    print(f"XGBoost Precision: {precision:.4f}")

    recall = recall_score(y_test, y_pred)
    print(f"XGBoost Recall: {recall:.4f}")

    f1 = f1_score(y_test, y_pred)
    print(f"XGBoost F1 Score: {f1:.4f}")

    y_prob = xgb_model.predict_proba(x_test)[:, 1]
    roc_auc = roc_auc_score(y_test, y_prob)
    print(f"XGBoost ROC-AUC: {roc_auc:.4f}")


def initialize_shap(xgb_model, x_train):
    # Initialize SHAP explainer
    print("Initializing SHAP tree explainer and calculating SHAP values...")
    explainer = shap.TreeExplainer(xgb_model)
    shap_values = explainer.shap_values(x_train)

    return explainer, shap_values

def shap_summary_plot(shap_values, x_train):
    # Create SHAP summary plot
    print("Generating SHAP summary plot...")
    shap.summary_plot(shap_values, x_train, plot_type="dot", dpi=150, show=False)
    plt.savefig("eda_charts/shap_summary_plot.png")
    plt.close()
    print("SHAP summary plot saved to eda_charts/shap_summary_plot.png")



