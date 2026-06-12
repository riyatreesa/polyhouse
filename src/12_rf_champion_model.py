# 12_rf_champion_model.py

import pandas as pd
import matplotlib.pyplot as plt

from joblib import load
from sklearn.model_selection import train_test_split
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
# Load tuned model
# -------------------------
champion = load(
    "models/random_forest_tuned.joblib"
)

# -------------------------
# Predictions
# -------------------------
pred = champion.predict(X_test)

# -------------------------
# Metrics
# -------------------------
tuned_rf_mae = mean_absolute_error(
    y_test,
    pred
)

tuned_rf_r2 = r2_score(
    y_test,
    pred
)

print(f"Tuned RF Test MAE: {tuned_rf_mae:.2f} kg")
print(f"Tuned RF Test R²:  {tuned_rf_r2:.3f}")

# -------------------------
# Predicted vs Actual plot
# -------------------------
plt.figure(figsize=(5, 5))

plt.scatter(
    y_test,
    pred,
    alpha=0.6
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)

plt.xlabel("Actual Yield (kg)")
plt.ylabel("Predicted Yield (kg)")
plt.title("Champion Model: Predicted vs Actual")

plt.tight_layout()

plt.savefig(
    "reports/figures/pred_vs_actual.png",
    dpi=150
)

print("Saved: reports/figures/pred_vs_actual.png")