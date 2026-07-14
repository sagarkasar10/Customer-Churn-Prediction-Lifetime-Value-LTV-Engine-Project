#import libraries
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler

 
# Load Dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\nDataset loaded successfully.")
        return df

    except FileNotFoundError:
        print("\nERROR: Dataset file not found!")
        print(f"Please check the file path:\n{file_path}")
        return None


#Inspect Dataset:
def data_info(df):
    print("\nDATASET INFORMATION:")
    
    print("\nShape of Dataset:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print ("\nFirst 5 rows:")
    print(df.head())


#cleaning dataset:
def clean_data(df):

    print("\nDATA CLEANING")

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].replace(" ", pd.NA),errors="coerce")

    # Fill missing values
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

    print("\nDataset cleaned successfully!")
    return df


#Train-Test split:
def data_split(df):
    print("\nTRAIN-TEST SPLIT:\n")

    X = df.drop(["customerID", "Churn"], axis=1)
    y=df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )
    print(f"Training Samples : {X_train.shape[0]}")
    print(f"Test Samples : {X_test.shape[0]}")
    return X_train, X_test, y_train, y_test


#Scaling dataset
def data_scaling(X_train, X_test):

    X_train = X_train.copy()
    X_test = X_test.copy()

    numerical_columns = [
        col for col in
        ["tenure", "MonthlyCharges", "TotalCharges"]
        if col in X_train.columns
    ]

    scaler = StandardScaler()

    X_train[numerical_columns] = scaler.fit_transform(
        X_train[numerical_columns]
    )

    X_test[numerical_columns] = scaler.transform(
        X_test[numerical_columns]
    )

    print("\nDATA SCALING")

    print("\nScaled Columns:")
    print(numerical_columns)

    return X_train, X_test, scaler


#Cross validation:
def cross_validation():
    print("\nCROSS VALIDATION:")

    cvalid = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42)
    
    print ("\nCross Validation created successfully!")
    return cvalid


#Main function:
def main():

    #start
    file_path = r"C:\Users\TIYA\Desktop\ZAALIMA\Customer-Churn-Prediction-Lifetime-Value-LTV-Engine-Project\WA_Fn-UseC_-Telco-Customer-Churn (1).csv"

    # Load dataset
    df = load_data(file_path)

    if df is None:
        return

    #inspect dataset
    data_info(df)

    #cleaning dataset
    df = clean_data(df)

   #train-test split
    X_train, X_test, y_train, y_test = data_split(df)
    print(f"\nX_train Shape: {X_train.shape}")
    print(f"\nX_test Shape : {X_test.shape}")
    print(f"\ny_train Shape: {y_train.shape}")
    print(f"\ny_test Shape : {y_test.shape}")

    #data Scaling
    X_train, X_test, scaler = data_scaling(
        X_train,
        X_test
    )

    #cross validation
    cvalid = cross_validation()
    print(cvalid)

    #complete
    print("\nDATA PREPARATION COMPLETED!")


if __name__ == "__main__":
    main()