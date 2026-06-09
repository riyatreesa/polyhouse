# 03_sample.py

import pandas as pd
from pathlib import Path

# Show all columns
pd.set_option("display.max_columns", None)

# Hide pandas index
pd.set_option("display.show_dimensions", False)

# Load cleaned data
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Add serial number
df.insert(0, "S.No", range(1, len(df) + 1))

# Take first 50 rows
sample = df.head(50)

# Print without index column (0–49)
print("\nFirst 50 Cleaned Rows:\n")
print(sample.to_string(index=False))

# Save CSV
Path("data/processed").mkdir(parents=True, exist_ok=True)

sample.to_csv(
    "data/processed/sample_cleaned_50_rows.csv",
    index=False
)

print("\nSaved: data/processed/sample_cleaned_50_rows.csv")