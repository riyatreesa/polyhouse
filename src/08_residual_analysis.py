# 08_residual_analysis.py

import pandas as pd
import joblib
import matplotlib.pyplot as plt
from pathlib import Path

# Create figures folder
Path("reports/figures").mkdir(
    parents=True,
    exist_ok=True
)

# Load data
df = pd.read_parquet(
    "data/processed/02_cleaned.parquet"
).sort_values("timestamp")

# Features and target
feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm"
]

X = df[feature_cols]
y = df["yield_kg"]

# Same split as linear regression
split_idx = int(len(df) * 0.8)

X_test = X.iloc[split_idx:]
y_test = y.iloc[split_idx:]

# Load scaler
scaler = joblib.load(
    "models/scaler.joblib"
)

X_test = scaler.transform(X_test)

# Load model
model = joblib.load(
    "models/linear_regression.joblib"
)

# Predictions
pred_test = model.predict(X_test)

# Residuals
residuals = y_test - pred_test

# Create plots
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Residuals vs Predicted
axes[0].scatter(pred_test, residuals, alpha=0.5)
axes[0].axhline(0, color="red", linestyle="--")
axes[0].set(
    xlabel="Predicted yield (kg)",
    ylabel="Residual (kg)"
)

# Residuals vs Humidity
axes[1].scatter(
    X_test[:, 1],
    residuals,
    alpha=0.5
)

axes[1].axhline(0, color="red", linestyle="--")
axes[1].set(
    xlabel="Scaled humidity",
    ylabel="Residual (kg)"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/residuals_linear.png",
    dpi=150
)

plt.show()

print("Saved: reports/figures/residuals_linear.png")
