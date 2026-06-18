import streamlit as st
import joblib
import pandas as pd
import numpy as np
from pathlib import Path

MODEL_DIR = Path("models")


@st.cache_resource
def load_model():
    return joblib.load(MODEL_DIR / "random_forest.joblib")


_model = load_model()


def predict_yield(
    temperature_c: float,
    humidity_pct: float,
    co2_ppm: float
) -> float:

    row = pd.DataFrame({
        "temperature_c": [temperature_c],
        "humidity_pct": [humidity_pct],
        "co2_ppm": [co2_ppm]
    })

    prediction = _model.predict(row)[0]

    return float(prediction)


def sensitivity_curve(
    humidity_pct: float,
    co2_ppm: float
):

    temperatures = np.linspace(10, 35, 50)

    predictions = []

    for temp in temperatures:

        pred = predict_yield(
            temp,
            humidity_pct,
            co2_ppm
        )

        predictions.append(pred)

    return temperatures, predictions