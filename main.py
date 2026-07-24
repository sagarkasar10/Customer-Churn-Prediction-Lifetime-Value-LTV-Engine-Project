import pandas as pd
from Preprocessing import preprocessing_data
from src.data_preparation import data_split, data_scaling
from feature_services import handle_missing_service_data, total_services_count, service_complexity_score, \
    create_tenure_cohorts, create_average_monthly_ratio, handle_outliers
from Model_logreg import logistic_regression_model, evaluate_logreg_model
from ensemble_random_forest import rf_model, evaluate_model, tune_rf, feature_importance_plot, compare_models
from xgb_model import train_xgboost_model, tuning_and_evaluation_xgb_model, initialize_shap, shap_summary_plot
import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)



# MAIN PIPELINE

def main():
    try:

        # 1. LOAD DATA

        print("\nLoading dataset...")

        df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn (1).csv')

        print(f"Dataset loaded successfully: {df.shape}")


        # 2. PREPROCESS & CLEAN DATA

        print("\nPreprocessing data...")

        preprocess_df = preprocessing_data(df)


        # 3. FEATURE ENGINEERING

        print("\nPerforming feature engineering...")

        # Handle missing service data
        feature1_df = handle_missing_service_data(preprocess_df)

        # Create total number of subscribed services
        feature2_df = total_services_count(feature1_df)

        # Create service complexity score
        feature3_df = service_complexity_score(feature2_df)

        # Create tenure cohorts
        feature4_df = create_tenure_cohorts(feature3_df)

        # Create average monthly charges / ratio features
        feature5_df = create_average_monthly_ratio(feature4_df)

        # Handle outliers
        feature_df = handle_outliers(feature5_df)

        print(
            f"Feature engineering completed. "
            f"Final shape: {feature_df.shape}")


        # 4. TRAIN TEST SPLIT

        # Encode Churn target explicitly (keep separate from feature dummies)
        feature_df["Churn"] = feature_df["Churn"].map({"Yes": 1, "No": 0})


        # Encode categorical feature columns only — exclude ID and target
        categorical_cols = [
            col for col in feature_df.select_dtypes(include=['object','category']).columns
            if col not in ['customerID', 'Churn']
        ]

        # Create dummy variables for categorical features, dropping the first category to avoid multicollinearity
        clean_df = pd.get_dummies(feature_df, columns=categorical_cols, drop_first=True)

        # Split the data into training and testing sets
        print("\nSplitting data...")

        X_train, X_test, y_train, y_test = data_split(clean_df)


        # 5. DATA SCALING

        print("\nScaling data...")

        X_train, X_test = data_scaling(X_train, X_test)


        # Model Training and Evaluation
        # 6. LOGISTIC REGRESSION

        print("\n==============================")

        print("LOGISTIC REGRESSION")

        print("==============================")

        best_model, y_pred, grid_search = logistic_regression_model(X_train, y_train, X_test, y_test)
        evaluate_logreg_model(y_test, y_pred, best_model, grid_search)


        # 7. RANDOM FOREST

        print("\n==============================")

        print("RANDOM FOREST")

        print("==============================")

        # 7.1 Train baseline Random Forest

        rf = rf_model(X_train, y_train)

        # 7.2 Evaluate baseline Random Forest

        baseline_metrics = evaluate_model(rf, X_test, y_test, label="Baseline RF")

        # 7.3 Feature importance

        feature_importances = feature_importance_plot(rf, X_train)

        # 7.4 Tune Random Forest

        tuned_rf = tune_rf(X_train, y_train)

        # 7.5 Evaluate tuned Random Forest

        tuned_metrics = evaluate_model(tuned_rf, X_test, y_test, label="Tuned RF")

        # 7.6 Compare baseline and tuned models

        comparison = compare_models(baseline_metrics, tuned_metrics)


        # 8. XGBOOST MODEL

        print("\n==============================")

        print("XGBOOST")

        print("==============================")

        xgboost_model = train_xgboost_model(X_train, y_train)

        tuning_and_evaluation_xgb_model(X_test, y_test, xgboost_model)


        # 9. SHAP ANALYSIS

        print("\n==============================")

        print("SHAP ANALYSIS")

        print("==============================")

        explainer, shap_values = initialize_shap(xgboost_model, X_train)


        # 10. SHAP SUMMARY PLOT

        shap_summary_plot(shap_values, X_train)


        # PIPELINE COMPLETED

        print("\n========================================")

        print("COMPLETE ML PIPELINE EXECUTED SUCCESSFULLY")

        print("========================================")


    except Exception as e:

        print(f"\nPipeline failed: {str(e)}")
        raise



# PROGRAM ENTRY POINT

if __name__ == "__main__":
    main()
