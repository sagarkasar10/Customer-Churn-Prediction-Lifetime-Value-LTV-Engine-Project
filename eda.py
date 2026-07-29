import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def churn_distribution(df):
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

    plt.tight_layout()
    plt.show()


def contract_vs_churn(df):
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

    plt.tight_layout()
    plt.show()