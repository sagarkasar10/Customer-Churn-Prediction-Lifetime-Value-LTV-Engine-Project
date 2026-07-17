import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix



#define the hyperparameter grid for logistic regression
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'solver': ['liblinear', 'lbfgs'],
    'max_iter': [300,500,1000]
}

#creates the logistic regression model
lr=LogisticRegression(random_state=42)

#creates the grid search object with cross-validation
grid_search = GridSearchCV(
    estimator=lr, 
    param_grid=param_grid,
    cv=5, scoring='f1', 
    n_jobs=-1)





df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn (1).csv")

# Separate features and target variable
df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())



# 5. Convert all remaining text columns into numeric 0 and 1 flags
X = df.drop(columns=['customerID', 'Churn'])
X = pd.get_dummies(X, drop_first=True)
print(df.head())
print(df.dtypes)
y = df['Churn']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train the model using grid search
grid_search.fit(X_train, y_train)

#get the best hyperparameters and the best model
best_model = grid_search.best_estimator_

#make predictions on the test set
y_pred = best_model.predict(X_test)



#evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))


#generate the confusion matrix
cm=confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)


#displaying confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)
plt.title("Logistic Regression Confusion Matrix")
plt.savefig("logistic_regression_confusion_matrix.png")
