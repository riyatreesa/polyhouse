import streamlit as st
import numpy as np
import pandas as pd
from src.predict import predict_yield

st.subheader("What-if: humidity sweep")

temp_fixed, co2_fixed = 22.0, 900
humid_range = np.linspace(70, 98, 29)

preds = [predict_yield(temp_fixed, h, co2_fixed) for h in humid_range]

chart_df = pd.DataFrame({
    "Humidity (%)": humid_range,
    "Predicted yield (kg)": preds
})

st.line_chart(
    chart_df,
    x="Humidity (%)",
    y="Predicted yield (kg)"
)

with st.expander("Model information"):

    st.markdown("""
    - **Model:** Tuned Random Forest
    - **Test MAE:** 1.2 kg/day
    - **Training data:** Polyhouse sensors Jan–Dec 2024
    """)