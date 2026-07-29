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

