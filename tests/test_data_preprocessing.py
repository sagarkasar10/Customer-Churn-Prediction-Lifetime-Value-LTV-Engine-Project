import pandas as pd
from Preprocessing import preprocessing_data

def test_preprocess_data():
    df = pd.DataFrame({
        "customerID": ["0001", "0002"],
        "SeniorCitizen": [0, 1],
        "TotalCharges": ["100", ""],
        "gender": ["Male", "Female"]
    })

    result = preprocessing_data(df)

    assert result is not None
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert result["SeniorCitizen"].tolist() == ["No", "Yes"]