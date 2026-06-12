# 10_rf_cv_comparison.py

import pandas as pd

from sklearn.model_selection import (
    train_test_split,
    TimeSeriesSplit,
    cross_val_score
)

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# -------------------------
# Load dataset
# -------------------------
df = pd.read_parquet(
    "data/processed/02_cleaned.parquet"
)

# -------------------------
# Features and target
# -------------------------
X = df[
    [
        "temperature_c",
        "humidity_pct",
        "co2_ppm"
    ]
]

y = df["yield_kg"]

# -------------------------
# Train-test split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------
# Models
# -------------------------
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

lin = LinearRegression()

# -------------------------
# TimeSeriesSplit
# -------------------------
tscv = TimeSeriesSplit(
    n_splits=5
)

# -------------------------
# Cross-validation scores
# -------------------------
rf_scores = cross_val_score(
    rf,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

lin_scores = cross_val_score(
    lin,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

# -------------------------
# Print results
# -------------------------
print(
    "RF CV MAE:",
    round((-rf_scores).mean(), 3),
    "+/-",
    round((-rf_scores).std(), 3)
)

print(
    "Linear CV MAE:",
    round((-lin_scores).mean(), 3),
    "+/-",
    round((-lin_scores).std(), 3)
)