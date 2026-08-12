import pandas as pd

def encode_target_and_categoricals(df):

    df = df.copy()

    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({
            "Yes": 1,
            "No": 0
        })

    categorical_cols = [
        col
        for col in df.select_dtypes(
            include=["object", "category", "string"]
        ).columns
        if col not in ["customerID", "Churn"]
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_cols,
        drop_first=True
    )

    return df