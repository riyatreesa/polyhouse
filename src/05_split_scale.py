# 05_split_scale.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
from pathlib import Path

# Create models folder
Path("models").mkdir(exist_ok=True)

# Load cleaned data
df = pd.read_parquet(
    "data/processed/02_cleaned.parquet"
).sort_values("timestamp")

# Feature columns
feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm"
]

# Feature matrix and target
X = df[feature_cols]
y = df["yield_kg"]

# Chronological train-test split
split_idx = int(len(df) * 0.8)

train = df.iloc[:split_idx]
test = df.iloc[split_idx:]

# Scale using TRAIN ONLY
scaler = MinMaxScaler()

X_train = scaler.fit_transform(train[feature_cols])
X_test = scaler.transform(test[feature_cols])

y_train = train["yield_kg"].values
y_test = test["yield_kg"].values

# Save scaler
joblib.dump(
    scaler,
    "models/scaler.joblib"
)

# Print summary
print("TRAIN SET")
print("Rows:", len(train))
print("Start:", train["timestamp"].min())
print("End:  ", train["timestamp"].max())

print("\nTEST SET")
print("Rows:", len(test))
print("Start:", test["timestamp"].min())
print("End:  ", test["timestamp"].max())

print("\nScaler saved:")
print("models/scaler.joblib")