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

def service_complexity_score(df):

    weights = {
        "PhoneService":1,
        "MultipleLines":1,
        "OnlineSecurity":3,
        "OnlineBackup":2,
        "DeviceProtection":2,
        "TechSupport":3,
        "StreamingTV":1,
        "StreamingMovies":1
    }

    score = 0

    for col, weight in weights.items():

        score += (
            df[col]
            .replace({
                "Yes":1,
                "No":0,
                "No internet service":0,
                "No phone service":0
            })
            * weight
        )

    df["ServiceComplexityScore"] = score

    return df


def create_service_features(df):

    df = handle_missing_service_data(df)

    df = total_services_count(df)

    df = service_complexity_score(df)

    return df
