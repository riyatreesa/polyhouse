import pandas as pd
from pathlib import Path

# Input CSV file
RAW = "data/raw/polyhouse_sensors.csv"

# Create interim folder
INTERIM = Path("data/interim")
INTERIM.mkdir(parents=True, exist_ok=True)

# Load CSV
df = pd.read_csv(
    RAW,
    parse_dates=["timestamp"]
)

# Display basic information
print("Shape:", df.shape)
print("\nFirst 5 rows:\n")
print(df.head())

# Save as parquet
df.to_parquet(
    "data/interim/01_loaded.parquet",
    index=False
)

print("\nSaved: data/interim/01_loaded.parquet")