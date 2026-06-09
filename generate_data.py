import pandas as pd
import numpy as np

np.random.seed(42)

days = pd.date_range("2025-01-01", periods=365)

temperature = np.random.normal(30, 3, 365)
humidity = np.random.normal(85, 6, 365)
co2 = np.random.normal(850, 80, 365)

# Yield pattern:
yield_kg = (
    18
    + 0.18 * (temperature - 30)      # positive effect
    + 0.05 * (humidity - 85)         # weak positive effect
    - 0.004 * (co2 - 850)            # weak negative effect
    + np.random.normal(0, 0.8, 365) # noise
)

df = pd.DataFrame({
    "timestamp": days,
    "temperature_c": temperature.round(2),
    "humidity_pct": humidity.round(2),
    "co2_ppm": co2.round(2),
    "yield_kg": yield_kg.round(2)
})

# Add some missing values
df.loc[[57, 148, 236, 329], "temperature_c"] = np.nan
df.loc[[58, 149, 237, 330], "humidity_pct"] = np.nan
df.loc[[59, 150, 238, 331], "co2_ppm"] = np.nan

df.to_csv("data/raw/polyhouse_sensor.csv", index=False)

print(df.head())