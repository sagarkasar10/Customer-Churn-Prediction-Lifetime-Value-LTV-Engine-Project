def customer():

    return {
        "gender":"Male",
        "SeniorCitizen":0,
        "Partner":"Yes",
        "Dependents":"No",
        "tenure":15,
        "PhoneService":"Yes",
        "MultipleLines":"No",
        "InternetService":"DSL",
        "OnlineSecurity":"Yes",
        "OnlineBackup":"No",
        "DeviceProtection":"Yes",
        "TechSupport":"No",
        "StreamingTV":"Yes",
        "StreamingMovies":"No",
        "Contract":"Month-to-month",
        "PaperlessBilling":"Yes",
        "PaymentMethod":"Electronic check",
        "MonthlyCharges":80,
        "TotalCharges":1200
    }


def test_batch_prediction(client):

    payload = [
        customer(),
        customer(),
        customer()
    ]

    response = client.post(
        "/predict/batch",
        json=payload
    )

    assert response.status_code == 200

    predictions = response.json()

    assert len(predictions) == 3

    for item in predictions:

        assert "predicted_ltv" in item
        assert "risk_tier" in item
        assert "churn_probability" in item