import pandas as pd
from pathlib import Path

# Create processed folder
PROCESSED = Path("data/processed")
PROCESSED.mkdir(parents=True, exist_ok=True)

# Load data from ingestion step
df = pd.read_parquet("data/interim/01_loaded.parquet")

# Show missing values before cleaning
print("Missing values before cleaning:")
print(df.isna().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df["temperature_c"] = df["temperature_c"].fillna(
    df["temperature_c"].mean()
)

df["humidity_pct"] = df["humidity_pct"].fillna(
    df["humidity_pct"].mean()
)

df["co2_ppm"] = df["co2_ppm"].fillna(
    df["co2_ppm"].mean()
)
# Add source file column
df["source_file"] = "polyhouse_sensor.csv"

# Save cleaned dataset
df.to_parquet(
    PROCESSED / "02_cleaned.parquet",
    index=False
)

# Create display copy with serial number
display_df = df.copy()
display_df.insert(0, "S.No", range(1, len(display_df) + 1))

# Show all columns
pd.set_option("display.max_columns", None)

# Display first 5 rows
print("\nFirst 5 Cleaned Rows:\n")
print(display_df.head().to_string(index=False))

print("\nClean rows:", len(df))
print("\nSaved: data/processed/02_cleaned.parquet")