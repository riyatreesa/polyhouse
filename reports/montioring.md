# Monitoring Plan

## Input and Prediction Log Sample

| Temperature (°C) | Humidity (%) | CO₂ (ppm) | Predicted Yield (kg) |
|-----------------|--------------|-----------|---------------------|
| 22.0 | 88.0 | 900 | 15.83 |
| 24.0 | 92.0 | 1100 | 16.21 |

## Model Artifact Handling

The trained model file `random_forest.joblib` is committed to the repository and loaded directly by the Streamlit application.

## Retraining Triggers

1. New sensor data becomes available.
2. Prediction accuracy decreases.
3. Data drift is detected.
4. Monthly review indicates degradation.

## Monitoring Frequency

Prediction logs should be reviewed monthly.