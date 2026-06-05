from pathlib import Path
import pandas as pd
from ingest import load_data

df = load_data()

sensor_columns = [
    "temperature",
    "humidity",
    "co2",
    "yield"
]

for col in sensor_columns:
    if col in df.columns:
        df[col] = df[col].interpolate(
            method="linear",
            limit_direction="both"
        )

Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)

df.to_parquet(
    "data/processed/02_cleaned.parquet",
    index=False
)

# SAVE ALL ROWS
df.to_csv(
    "data/processed/sample_cleaned_50_rows.csv",
    index=False
)

print("Rows Saved:", len(df))
print("Cleaning complete!")