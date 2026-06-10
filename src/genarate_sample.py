import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

# Number of records
n = 365

# Generate sensor values
temp = rng.normal(22, 1.5, n)
hum = np.clip(rng.normal(87, 3, n), 75, 98)
co2 = rng.normal(900, 80, n)

# Generate yield with randomness
yield_kg = (
    8
    + 0.30 * temp
    + 0.03 * hum
    - 0.001 * co2
    + rng.normal(0, 1.0, n)
)

# Create DataFrame
df = pd.DataFrame({
    "timestamp": pd.date_range("2024-01-01", periods=n, freq="D"),
    "temperature_c": temp.round(2),
    "humidity_pct": hum.round(1),
    "co2_ppm": co2.round(0),
    "yield_kg": yield_kg.round(2)
})

# -------------------------
# Add missing values
# -------------------------
df.loc[[50, 120, 250], "temperature_c"] = np.nan
df.loc[[80, 180], "humidity_pct"] = np.nan
df.loc[[150, 300], "co2_ppm"] = np.nan

# -------------------------
# Add duplicate rows
# -------------------------
duplicates = df.iloc[[10, 25, 40]]
df = pd.concat([df, duplicates], ignore_index=True)

# Save CSV
df.to_csv(
    "data/raw/polyhouse_sensors.csv",
    index=False
)

print("Synthetic dataset generated successfully!")
print("\nShape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nFirst 5 rows:")
print(df.head())