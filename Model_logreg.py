import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score

def logistic_regression_model(X_train, y_train, X_test, y_test):
    #define the hyperparameter grid for logistic regression
    param_grid = {
        'C': [0.01, 0.1, 1, 10, 100],
        'solver': ['liblinear', 'lbfgs'],
        'max_iter': [300,500,1000,2000]
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
    grid_search.fit(X_train, y_train)

    #get the best hyperparameters and the best model
    best_model = grid_search.best_estimator_

    #make predictions on the test set
    y_pred = best_model.predict(X_test)
    return best_model, y_pred, grid_search


def evaluate_logreg_model(X_test,y_test, y_pred, best_model, grid_search):
    #evaluate the model
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))
    y_proba = best_model.predict_proba(X_test)[:, 1]
    roc_auc = roc_auc_score(y_test, y_proba)
    print("ROC AUC Score:", roc_auc)


    #generate the confusion matrix
    cm=confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)


    #displaying confusion matrix
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Logistic Regression Confusion Matrix")
    # plt.savefig("logistic_regression_confusion_matrix.png")

    #save the best trained model
    joblib.dump(best_model, "best_logistic_regression_model.pkl")
    print("Best Logistic Regression model saved as 'best_logistic_regression_model.pkl'")
    print("Confusion matrix saved as 'logistic_regression_confusion_matrix.png'")



    #save best hyperparameters to a text file
    print("Best hyperparameters:", grid_search.best_params_)
    print("Best cross-validation f1 score:", grid_search.best_score_)
