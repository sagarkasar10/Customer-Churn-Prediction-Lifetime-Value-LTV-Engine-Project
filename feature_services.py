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


def create_tenure_cohorts(df):
    """
    Groups customers based on tenure.
    """

    bins = [0, 12, 24, 48, 60, np.inf]

    labels = [
        "0-12 Months",
        "13-24 Months",
        "25-48 Months",
        "49-60 Months",
        "60+ Months"
    ]

    df["TenureCohort"] = pd.cut(
        df["tenure"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    return df


def create_average_monthly_ratio(df):
    """
    Average Monthly Ratio =
    TotalCharges / tenure

    Handles customers with zero tenure.
    """

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df["AverageMonthlyRatio"] = np.where(
        df["tenure"] == 0,
        df["MonthlyCharges"],
        df["TotalCharges"] / df["tenure"]
    )

    return df


