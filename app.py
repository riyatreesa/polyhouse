import streamlit as st
import matplotlib.pyplot as plt

from src.predict import (
    predict_yield,
    sensitivity_curve
)

st.set_page_config(
    page_title="Mushroom Yield Forecast",
    layout="centered"
)

st.title("🍄 Mushroom Yield Predictor")
st.caption("Agritech environmental forecasting from sensor data")

# -------------------------
# Sidebar Inputs
# -------------------------
with st.sidebar:

    st.header("Sensor Readings")

    temp = st.slider(
        "Temperature (°C)",
        10.0,
        35.0,
        22.0,
        0.1
    )

    humid = st.slider(
        "Humidity (%)",
        50.0,
        100.0,
        88.0,
        0.5
    )

    co2 = st.slider(
        "CO₂ (ppm)",
        400,
        2000,
        900,
        10
    )

# -------------------------
# Prediction
# -------------------------
if st.button("Predict Yield"):

    kg = predict_yield(
        temp,
        humid,
        co2
    )

    st.metric(
        label="Estimated Daily Yield",
        value=f"{kg:.2f} kg"
    )

    # -------------------------
    # Sensitivity Chart
    # -------------------------
    st.subheader("Sensitivity Analysis")

    temperatures, predictions = sensitivity_curve(
        humid,
        co2
    )

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(
        temperatures,
        predictions
    )

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Predicted Yield (kg)")
    ax.set_title("Effect of Temperature on Yield")

    ax.grid(True)

    st.pyplot(fig)