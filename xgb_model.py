import xgboost as xgb
import shap 
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score


def train_xgboost_model(x_train, y_train):
    # Initialize the XGBoost classifier
    xgb_model = xgb.XGBClassifier(eval_metric='logloss', random_state=42)

    # Train the model
    xgb_model.fit(x_train, y_train)

    print("XGBoost Model trained successfully!")

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

def shap_summary_plot(shap_values, x_train):
    # Create SHAP summary plot
    print("Generating SHAP summary plot...")
    shap.summary_plot(shap_values, x_train, plot_type="bar")
    plt.show()
    #plt.savefig("shap_summary_plot.png")



