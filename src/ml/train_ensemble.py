import pickle
from sklearn.ensemble import RandomForestRegressor
from prepare_data import get_processed_data


def train_ensemble():
    print("--- Training Ensemble Random Forest ---")

    # 1. Load split data
    X_train, X_test, y_train, y_test = get_processed_data()

    # 2. Train model
    ensemble_model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    ensemble_model.fit(X_train, y_train)

    print("Ensemble Random Forest Regressor trained successfully")
    print(f"Train score (R²): {ensemble_model.score(X_train, y_train):.4f}")
    print(f"Test score (R²): {ensemble_model.score(X_test, y_test):.4f}")

    # 3. Pickle artifact
    model_path = "ensemble_regressor.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(ensemble_model, f)

    print(f"Saved model to: {model_path}\n")


if __name__ == "__main__":
    train_ensemble()