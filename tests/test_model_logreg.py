from Model_logreg import logistic_regression_model, evaluate_logreg_model
def test_logistic_regression_model_function_exists():
    # Test if the logistic_regression_model function exists
    assert callable(logistic_regression_model)

def test_evaluate_logreg_model_function_exists():
    # Test if the evaluate_logreg_model function exists
    assert callable(evaluate_logreg_model)