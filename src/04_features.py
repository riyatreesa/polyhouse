# 04_features.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
from pathlib import Path

# Create models folder
Path("models").mkdir(exist_ok=True)

# Load cleaned dataset
df = pd.read_parquet(
    "data/processed/02_cleaned.parquet"
).sort_values("timestamp")

# Feature engineering
df["temp_humid_interaction"] = (
    df["temperature_c"] * df["humidity_pct"] / 100
)

# Feature matrix and target
feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction"
]

X = df[feature_cols]
y = df["yield_kg"]

# Scale features (for learning purposes only)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Save scaler
joblib.dump(
    scaler,
    "models/minmax_scaler.joblib"
)

# Create processed dataframe
processed = pd.DataFrame(
    X_scaled,
    columns=[c + "_scaled" for c in feature_cols]
)

processed["yield_kg"] = y.values

# Save engineered dataset
processed.to_parquet(
    "data/processed/features.parquet",
    index=False
)

print("Feature engineering completed.")
print("Saved: data/processed/features.parquet")