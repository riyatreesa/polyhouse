import pandas as pd
from pathlib import Path

# Load cleaned data
df = pd.read_parquet(
    "data/processed/02_cleaned.parquet"
).sort_values("timestamp")

# Chronological split
split_idx = int(len(df) * 0.8)

train = df.iloc[:split_idx]
test = df.iloc[split_idx:]

# README content
readme_content = f"""# Polyhouse Yield Prediction

## Feature Engineering

An interaction feature was created:

- temp_humid_interaction = temperature_c × humidity_pct / 100

Features used:

- temperature_c
- humidity_pct
- co2_ppm
- temp_humid_interaction

Target variable:

- yield_kg

---

## Train-Test Split Summary

The dataset was sorted chronologically using the timestamp column and split using an 80:20 ratio.

### Training Set
- Rows: {len(train)}
- Start Date: {train['timestamp'].min()}
- End Date: {train['timestamp'].max()}

### Testing Set
- Rows: {len(test)}
- Start Date: {test['timestamp'].min()}
- End Date: {test['timestamp'].max()}

---

## Feature Scaling

MinMaxScaler was used to normalize the features.

To avoid data leakage, the scaler was fitted only on the training data and then applied to the test data.

Scaler saved to:

models/scaler.joblib
"""

# Write README
with open("POLYHOUSE_YIELD_PREDICTION_README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("POLYHOUSE_YIELD_PREDICTION_README.md generated successfully.")