# 07_linear_regression.py

import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path

from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Create folders
Path("models").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)

# Load cleaned data
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

# Time-based split
split_idx = int(len(df) * 0.8)

X_train = X.iloc[:split_idx]
X_test = X.iloc[split_idx:]

y_train = y.iloc[:split_idx]
y_test = y.iloc[split_idx:]

# Scale using train data only
scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
pred_test = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, pred_test)
rmse = np.sqrt(mean_squared_error(y_test, pred_test))
r2 = r2_score(y_test, pred_test)

print(f"Test MAE:  {mae:.2f} kg")
print(f"Test RMSE: {rmse:.2f} kg")
print(f"Test R²:   {r2:.3f}")

# Feature coefficients
for name, coef in zip(
    ["temp", "humidity", "co2"],
    model.coef_
):
    print(f"coef {name}: {coef:.3f}")

# Save metrics
metrics = {
    "MAE": round(mae, 2),
    "RMSE": round(rmse, 2),
    "R2": round(r2, 3)
}

with open(
    "reports/linear_metrics.json",
    "w"
) as f:
    json.dump(metrics, f, indent=4)

print("Saved: reports/linear_metrics.json")

# Save model
joblib.dump(
    model,
    "models/linear_regression.joblib"
)

print("Saved: models/linear_regression.joblib")