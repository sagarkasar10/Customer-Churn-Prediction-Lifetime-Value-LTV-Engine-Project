import pandas as pd

SERVICE_COLUMNS = [
    "PhoneService",
    "MultipleLines",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies"
]


def handle_missing_service_data(df):

    for col in SERVICE_COLUMNS:
        df[col] = df[col].fillna("No")

    return df


def total_services_count(df):

    temp = df[SERVICE_COLUMNS].replace({
        "Yes":1,
        "No":0,
        "No internet service":0,
        "No phone service":0
    })

    df["TotalServices"] = temp.sum(axis=1)

    return df