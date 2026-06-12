# 09_train_random_forest.py

import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

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
# Train Random Forest
# -------------------------
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

# -------------------------
# Predictions
# -------------------------
pred = rf.predict(X_test)

# -------------------------
# Metrics
# -------------------------
rf_mae = mean_absolute_error(
    y_test,
    pred
)

rf_r2 = r2_score(
    y_test,
    pred
)

print(f"RF Test MAE: {rf_mae:.2f} kg")
print(f"RF Test R²:  {rf_r2:.3f}")

# -------------------------
# Feature Importance
# -------------------------
importances = rf.feature_importances_

labels = [
    "temperature",
    "humidity",
    "co2"
]

plt.figure(figsize=(6, 4))

plt.barh(
    labels,
    importances
)

plt.xlabel("Importance")
plt.title("Random Forest Feature Importance")

plt.tight_layout()

plt.savefig(
    "reports/figures/rf_importance.png",
    dpi=150
)

# -------------------------
# Save model
# -------------------------
joblib.dump(
    rf,
    "models/random_forest.joblib"
)

print("Saved: reports/figures/rf_importance.png")
print("Saved: models/random_forest.joblib")