import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

EDA_CHARTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "eda_charts")


def _finish_plot(filename: str, show: bool = False):
    os.makedirs(EDA_CHARTS, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(EDA_CHARTS, filename), dpi=150)
    if show:
        plt.show()
    plt.close()

def dataset_overview(df):
    """
    Display basic information about the dataset.
    """

    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print(f"Number of rows    : {df.shape[0]}")
    print(f"Number of columns : {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())


def missing_value_analysis(df):
    """
    Analyze missing values in the dataset.
    """

    print("\n" + "=" * 60)
    print("MISSING VALUE ANALYSIS")
    print("=" * 60)

    missing_values = df.isnull().sum()

    missing_values = missing_values[
        missing_values > 0
    ].sort_values(ascending=False)

    if missing_values.empty:
        print("No missing values found.")
    else:
        print(missing_values)

    print("\nTotal Missing Values:", df.isnull().sum().sum())

def churn_distribution(df, show=False):
    """
    Analyze the distribution of customers who churned
    and customers who did not churn.
    """

    print("\n" + "=" * 60)
    print("CHURN DISTRIBUTION")
    print("=" * 60)

    churn_counts = df["Churn"].value_counts()
    churn_percentage = df["Churn"].value_counts(normalize=True) * 100

    print("\nCustomer Count:")
    print(churn_counts)

    print("\nChurn Percentage:")
    print(churn_percentage.round(2))

    plt.figure(figsize=(7, 5))

    sns.countplot(
        data=df,
        x="Churn"
    )

    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")

    _finish_plot("churn_distribution.png", show)


def contract_vs_churn(df, show=False):
    """
    Analyze the relationship between contract type and churn.
    """

    print("\n" + "=" * 60)
    print("CONTRACT TYPE VS CHURN")
    print("=" * 60)

    contract_churn = pd.crosstab(
        df["Contract"],
        df["Churn"],
        normalize="index"
    ) * 100

    print("\nChurn Percentage by Contract Type:")
    print(contract_churn.round(2))

    plt.figure(figsize=(9, 6))

    sns.countplot(
        data=df,
        x="Contract",
        hue="Churn"
    )

    plt.title("Contract Type vs Customer Churn")
    plt.xlabel("Contract Type")
    plt.ylabel("Number of Customers")

    plt.xticks(rotation=15)

    _finish_plot("contract_vs_churn.png", show)

def tenure_vs_churn(df, show=False):
    """
    Analyze the relationship between customer tenure
    and churn.
    """
    print("\n" + "=" * 60)
    print("TENURE VS CHURN")
    print("=" * 60)

    if "tenure" not in df.columns:
        print("Column 'tenure' not found.")
        return
    
    tenure_summary = df.groupby("Churn")["tenure"].agg(
        ["mean", "median", "min", "max"]
    )

    print("\nTenure Statistics by Churn:")
    print(tenure_summary.round(2))
    plt.figure(figsize=(9, 6))
    sns.boxplot(
        data=df,
        x="Churn",
        y="tenure"
    )

    plt.title("Customer Tenure vs Churn")
    plt.xlabel("Churn")
    plt.ylabel("Tenure (Months)")
    _finish_plot("tenure_vs_churn.png", show)


def tenure_cohort_vs_churn(df, show=False):

    """
    Group customers into tenure cohorts and analyze
    churn rate for each cohort.
    """

    print("\n" + "=" * 60)
    print("TENURE COHORT VS CHURN")
    print("=" * 60)

    if "tenure" not in df.columns:
        print("Column 'tenure' not found.")
        return

    df_eda = df.copy()
    df_eda["TenureCohort"] = pd.cut(
    df_eda["tenure"],
        bins=[-1, 12, 24, 48, 72],
        labels=[
            "0-12 Months",
            "13-24 Months",
            "25-48 Months",
            "49-72 Months"
        ]
    )

    cohort_churn = pd.crosstab(
        df_eda["TenureCohort"],
        df_eda["Churn"],
        normalize="index"
    ) * 100
    print("\nChurn Percentage by Tenure Cohort:")
    print(cohort_churn.round(2))
    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=df_eda,
        x="TenureCohort",
        hue="Churn"
    )
    
    plt.title("Tenure Cohort vs Customer Churn")
    plt.xlabel("Tenure Cohort")
    plt.ylabel("Number of Customers")
    _finish_plot("tenure_cohort_vs_churn.png", show)

def monthly_charges_vs_churn(df, show=False):
    """
    Analyze the relationship between monthly charges
    and customer churn.
    """

    print("\n" + "=" * 60)
    print("MONTHLY CHARGES VS CHURN")
    print("=" * 60)

    if "MonthlyCharges" not in df.columns:
        print("Column 'MonthlyCharges' not found.")
        return

    charges_summary = df.groupby("Churn")["MonthlyCharges"].agg(
        ["mean", "median", "min", "max"]
    )

    print("\nMonthly Charges Statistics by Churn:")
    print(charges_summary.round(2))

    plt.figure(figsize=(9, 6))

    sns.boxplot(
        data=df,
        x="Churn",
        y="MonthlyCharges"
    )

    plt.title("Monthly Charges vs Customer Churn")
    plt.xlabel("Churn")
    plt.ylabel("Monthly Charges")

    _finish_plot("monthly_charges_vs_churn.png", show)


def payment_method_vs_churn(df, show=False):
    """
    Analyze the relationship between payment method
    and customer churn.
    """

    print("\n" + "=" * 60)
    print("PAYMENT METHOD VS CHURN")
    print("=" * 60)

    if "PaymentMethod" not in df.columns:
        print("Column 'PaymentMethod' not found.")
        return

    payment_churn = pd.crosstab(
        df["PaymentMethod"],
        df["Churn"],
        normalize="index"
    ) * 100

    print("\nChurn Percentage by Payment Method:")
    print(payment_churn.round(2))

    plt.figure(figsize=(11, 6))

    sns.countplot(
        data=df,
        x="PaymentMethod",
        hue="Churn"
    )

    plt.title("Payment Method vs Customer Churn")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Customers")

    plt.xticks(rotation=30, ha="right")

    _finish_plot("payment_method_vs_churn.png", show)

def internet_service_vs_churn(df, show=False):
    """
    Analyze the relationship between internet service
    type and customer churn.
    """

    print("\n" + "=" * 60)
    print("INTERNET SERVICE VS CHURN")
    print("=" * 60)

    if "InternetService" not in df.columns:
        print("Column 'InternetService' not found.")
        return

    internet_churn = pd.crosstab(
        df["InternetService"],
        df["Churn"],
        normalize="index"
    ) * 100

    print("\nChurn Percentage by Internet Service:")
    print(internet_churn.round(2))

    plt.figure(figsize=(9, 6))

    sns.countplot(
        data=df,
        x="InternetService",
        hue="Churn"
    )

    plt.title("Internet Service vs Customer Churn")
    plt.xlabel("Internet Service")
    plt.ylabel("Number of Customers")

    _finish_plot("internet_service_vs_churn.png", show)


def numerical_correlation_analysis(df, show=False):
    """
    Analyze correlations between numerical variables.
    """

    print("\n" + "=" * 60)
    print("NUMERICAL CORRELATION ANALYSIS")
    print("=" * 60)

    numerical_df = df.select_dtypes(
        include=["int64", "float64"]
    )

    correlation_matrix = numerical_df.corr()

    print("\nCorrelation Matrix:")
    print(correlation_matrix.round(2))

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Numerical Features Correlation Heatmap")

    _finish_plot("numerical_correlation_heatmap.png", show)


def generate_baseline_summary(df):
    """
    Generate a baseline analytics summary for Week 1.
    """

    print("\n" + "=" * 60)
    print("BASELINE ANALYTICS SUMMARY")
    print("=" * 60)

    total_customers = len(df)

    churned_customers = (
        df["Churn"] == "Yes"
    ).sum()

    non_churned_customers = (
        df["Churn"] == "No"
    ).sum()

    churn_rate = (
        churned_customers / total_customers
    ) * 100

    print(f"\nTotal Customers       : {total_customers}")
    print(f"Churned Customers     : {churned_customers}")
    print(f"Non-Churned Customers : {non_churned_customers}")
    print(f"Overall Churn Rate    : {churn_rate:.2f}%")

    print("\nBaseline analytics generated successfully.")


def run_eda(df, show=False):
    """
    Run the complete Week 1 EDA pipeline. Charts are saved to eda_charts/;
    pass show=True to also display them interactively.
    """
    if not show:
        matplotlib.use("Agg", force=True)

    print("\n")
    print("=" * 60)
    print("STARTING EXPLORATORY DATA ANALYSIS")
    print("=" * 60)

    dataset_overview(df)

    missing_value_analysis(df)

    churn_distribution(df, show)

    contract_vs_churn(df, show)

    tenure_vs_churn(df, show)

    tenure_cohort_vs_churn(df, show)

    monthly_charges_vs_churn(df, show)

    payment_method_vs_churn(df, show)

    internet_service_vs_churn(df, show)

    numerical_correlation_analysis(df, show)

    generate_baseline_summary(df)

    print("\n" + "=" * 60)
    print(f"EDA COMPLETED SUCCESSFULLY — charts saved to {EDA_CHARTS}")
    print("=" * 60)