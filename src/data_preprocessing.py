import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold


#Load Dataset:
def load_data(file_path):
    df = pd.read_csv(file_path)
    print("\nDATA LOADED SUCCESSFULLY!")
    return df


#Inspect Dataset:
def data_info(df):
    print("\n")
    print("DATASET INFORMATION:")
    
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


#Cross validation:
def cross_validation():
    print("\nCROSS VALIDATION:\n")

    cvalid = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42)
    
    print ("Cross Validation created successfully!")
    return cvalid



#Main function:
def main():

    #started
    file_path = r"C:\Users\TIYA\Desktop\ZAALIMA\Customer-Churn-Prediction-Lifetime-Value-LTV-Engine-Project\WA_Fn-UseC_-Telco-Customer-Churn (1).csv"

    #load dataset
    df = load_data(file_path)

    #inspect dataset
    data_info(df)

   #train-test split
    X_train, X_test, y_train, y_test = data_split(df)
    print(f"\nX_train Shape: {X_train.shape}")
    print(f"\nX_test Shape : {X_test.shape}")
    print(f"\ny_train Shape: {y_train.shape}")
    print(f"\ny_test Shape : {y_test.shape}")

    #cross validation
    cvalid = cross_validation()
    print(cvalid)

    #completed
    print("\nDATA PREPARATION COMPLETED!")



if __name__ == "__main__":
    main()