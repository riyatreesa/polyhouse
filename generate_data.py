import pandas as pd
import numpy as np

# Reproducible random numbers
np.random.seed(42)

n = 300

temperature = np.random.normal(30, 3, n)
humidity = np.random.normal(85, 8, n)
co2 = np.random.normal(850, 80, n)

yield_kg = (
    8
    + 0.25 * temperature
    + 0.04 * humidity
    - 0.001 * co2
    + np.random.normal(0, 0.8, n)
)

df = pd.DataFrame({
    "temperature": temperature.round(2),
    "humidity": humidity.round(2),
    "co2": co2.round(2),
    "yield": yield_kg.round(2)
})

df.to_csv("data/raw/polyhouse_sensor.csv", index=False)

print("Dataset regenerated successfully.")