# tests/test_predict.py

from src.predict import predict_yield


def test_predict_returns_float_in_range():

    result = predict_yield(
        22.0,
        88.0,
        920
    )

    assert isinstance(result, float)
    assert 0 < result < 50


def test_prediction_changes_with_humidity():

    low_humidity = predict_yield(
        22.0,
        75.0,
        920
    )

    high_humidity = predict_yield(
        22.0,
        92.0,
        920
    )

    assert low_humidity != high_humidity


def test_prediction_changes_with_temperature():

    low_temp = predict_yield(
        18.0,
        88.0,
        920
    )

    high_temp = predict_yield(
        28.0,
        88.0,
        920
    )

    assert low_temp != high_temp