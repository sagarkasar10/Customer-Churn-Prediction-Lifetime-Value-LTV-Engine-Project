#import libraries
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
 

#Train-Test split:
def data_split(df):
    """
    Split the dataset into training and testing sets.
    """
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
    """
    Scale numerical features using StandardScaler.
    """
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

    return X_train, X_test


#Cross validation:
def cross_validation():
    """
    Create a Stratified K-Fold cross-validation object.
    """
    print("\nCROSS VALIDATION:")

    cvalid = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42)
    
    print ("\nCross Validation created successfully!")
    return cvalid