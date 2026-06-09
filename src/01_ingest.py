# 01_ingest.py

import pandas as pd
from pathlib import Path

# Paths
RAW = Path("data/raw/polyhouse_sensor.csv")
INTERIM = Path("data/interim")
INTERIM.mkdir(parents=True, exist_ok=True)

# Read CSV normally
df = pd.read_csv(RAW)

# Convert timestamp column
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Remove % sign from humidity values
df["humidity_pct"] = (
    df["humidity_pct"]
    .astype(str)
    .str.replace("%", "", regex=False)
)

# Convert all numeric columns
numeric_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "yield_kg"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Show outputs
print("Shape:")
print(df.shape)

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isna().sum())

# Save parquet file
df.to_parquet(INTERIM / "01_loaded.parquet", index=False)

print("\nSaved: data/interim/01_loaded.parquet")