from soothsayer.prediction import PredictionService

def test_predict_should_return_prediction_result():
    prediction_service = PredictionService()
    result = prediction_service.predict("This is a test")
    assert type(result.text) is str
    assert type(result.value) is str
    assert type(result.score) is float