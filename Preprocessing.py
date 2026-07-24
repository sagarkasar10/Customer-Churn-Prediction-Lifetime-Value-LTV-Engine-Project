import pandas as pd
import numpy as np

def preprocessing_data(df):
    # Display the first few rows of the dataset 
    print("Initial dataset preview:")
    print(df.head())

    # Display the shape of the dataset and check for missing values
    print("\nDataset shape:", df.shape)
    
    print("\nNaN counts:\n", df.isnull().sum()[df.isnull().sum() > 0])

    # Check for blank values in object type columns
    for col in df.select_dtypes(include='object').columns:
        blanks = df[col].astype(str).str.strip().eq('').sum()
        if blanks > 0:
            print(f"{col}: {blanks} blank values")

    # ---- Clean ----

    # Strip whitespace from all text columns
    str_cols = df.select_dtypes(include='object').columns
    for col in str_cols:
        df[col] = df[col].str.strip()


    # Checking for duplicate rows
    duplicate_rows = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicate_rows}")

    # Checking for duplicate customer id
    duplicate_customerid = df["customerID"].duplicated().sum()
    print(f"Duplicate customer IDs: {duplicate_customerid}")

    # Remove duplicate rows
    if duplicate_rows > 0:
        df.drop_duplicates(inplace=True)
        print(f"{duplicate_rows} duplicate rows removed successfully")
    else:
        print("No duplicate rows.")

    # Duplicate customer id still exists or not
    duplicate_customerid = df["customerID"].duplicated().sum()

    if duplicate_customerid>0:
        print(f"{duplicate_customerid} duplicate customer ids still exist.")
    else:
        print ("No duplicate customer id")

    #--------cleaning senior citizen column-----------
    print("\n values before cleaning senior citizen column:\n", df['SeniorCitizen'].unique())

    # convert 0 and 1 to No and Yes
    df["SeniorCitizen"]= df["SeniorCitizen"].replace({0: "No", 1: "Yes"})
    print("\n values after cleaning senior citizen column:\n", df['SeniorCitizen'].unique())

    # Convert 'TotalCharges' to numeric, coercing errors to NaN
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')

    # Check for missing values
    print("Missing values in TotalCharges:", df['TotalCharges'].isnull().sum())

    # Fill missing values in 'TotalCharges' with the median of the column
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

    # Check for missing values after filling
    print("Missing values in TotalCharges after filling:", df['TotalCharges'].isnull().sum())

    return df


