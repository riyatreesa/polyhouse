# Polyhouse Yield Prediction

## Feature Engineering

An interaction feature was created:

- temp_humid_interaction = temperature_c × humidity_pct / 100

Features used:

- temperature_c
- humidity_pct
- co2_ppm
- temp_humid_interaction

Target variable:

- yield_kg

---

## Train-Test Split Summary

The dataset was sorted chronologically using the timestamp column and split using an 80:20 ratio.

### Training Set
- Rows: 286
- Start Date: 2024-01-01 00:00:00
- End Date: 2024-10-18 00:00:00

### Testing Set
- Rows: 72
- Start Date: 2024-10-19 00:00:00
- End Date: 2024-12-30 00:00:00

---

## Feature Scaling

MinMaxScaler was used to normalize the features.

To avoid data leakage, the scaler was fitted only on the training data and then applied to the test data.

Scaler saved to:

models/scaler.joblib
