def sample_payload():

    return {
        "customerID": "0002-TEST",
        "gender":"Male",
        "SeniorCitizen":0,
        "Partner":"Yes",
        "Dependents":"No",
        "tenure":12,
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
        "MonthlyCharges":75.5,
        "TotalCharges":906
    }


def test_single_prediction(client):

    response = client.post(
        "/predict/single",
        json=sample_payload()
    )

    assert response.status_code == 200

    data = response.json()

    assert "churn_probability" in data
    assert "predicted_ltv" in data
    assert "risk_tier" in data