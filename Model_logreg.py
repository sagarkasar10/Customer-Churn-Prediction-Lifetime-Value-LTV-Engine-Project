from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import pandas as pd

#define the hyperparameter grid for logistic regression
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'solver': ['liblinear', 'lbfgs'],
    'max_iter': [100, 200, 300]
}

#creates the logistic regression model
lr=LogisticRegression(random_state=42)

#creates the grid search object with cross-validation
grid_search = GridSearchCV(
    estimator=lr, 
    param_grid=param_grid,
    cv=5, scoring='f1', 
    n_jobs=-1)

#train the model using grid search
from sklearn.model_selection import train_test_split


df = pd.read_csv(r"C:\Users\SA\Downloads\zaalima\Customer-Churn-Prediction-Lifetime-Value-LTV-Engine-Project\WA_Fn-UseC_-Telco-Customer-Churn (1).csv")
print(df.dtypes)
X = df.drop(columns=['customerID', 'Churn'])
y = df['Churn']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

grid_search.fit(X_train, y_train)

#get the best hyperparameters and the best model
best_model = grid_search.best_estimator_

#make predictions on the test set
y_pred = best_model.predict(X_test)

#import evaluation metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


#evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
